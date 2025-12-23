import asyncio
from typing import List
from warframe_market.client import WarframeMarketClient
from warframe_market.api.item import Items, Item


class ItemWithPrice:
    name: str
    slug: str
    platinum: float

    def __init__(self, name: str, slug: str, platinum: float):
        self.name = name
        self.slug = slug
        self.platinum = platinum

    def __str__(self):
        return f"{self.name}: {round(self.platinum, 2)}p"


async def fetch_price(
    client: WarframeMarketClient, itemName: str, itemSlug: str, sem: asyncio.Semaphore
):
    async with sem:
        for attempt in range(5):
            try:
                await asyncio.sleep(0.35)

                top_orders = await client.get_top_orders_for_item(itemSlug)
                buy_data = top_orders.data.buy

                if not buy_data:
                    return ItemWithPrice(itemName, itemSlug, 0)

                total_plat = sum(data.platinum for data in buy_data)
                avg_price = total_plat / len(buy_data)
                return ItemWithPrice(itemName, itemSlug, avg_price)

            except Exception as e:
                if "429" in str(e):
                    wait_time = (attempt + 1) * 2
                    print(f"Debug: Rate limited on {itemSlug}. Waiting {wait_time}s...")
                    await asyncio.sleep(wait_time)
                    continue
                else:
                    raise e

        raise Exception("Could not fetch item")


async def get_all_item_set_buy_prices(
    client: WarframeMarketClient,
) -> List[ItemWithPrice]:
    items = await client.get_all_items()
    itemSetsWithNames: list[tuple[str, str]] = []
    for item in items.data:
        name_low = item.i18n["en"].name.lower()
        slug_low = item.slug.lower()

        if ("set" in slug_low) or ("set" in name_low):
            itemSetsWithNames.append((item.i18n["en"].name, item.slug))

    # Limit concurrent requests to avoid rate limiting
    sem = asyncio.Semaphore(5)

    tasks = [fetch_price(client, name, slug, sem) for name, slug in itemSetsWithNames]
    results = await asyncio.gather(*tasks)

    itemWithPrices = [r for r in results if r is not None and r.platinum > 0]

    itemWithPrices.sort(key=lambda x: x.platinum, reverse=True)

    return itemWithPrices


async def main():
    async with WarframeMarketClient() as client:
        itemSets = await get_all_item_set_buy_prices(client)

        with open("out.txt", "w", encoding="utf-8") as f:
            for item in itemSets:
                f.write(f"{item}\n")

        print(f"Saved {len(itemSets)} items to out.txt")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
