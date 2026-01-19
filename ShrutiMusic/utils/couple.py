coupledb = {}


async def _get_lovers(cid: int):
    chat_data = coupledb.get(cid, {})
    lovers = chat_data.get("off", {})
    return lovers


async def get_image(cid: int):
    chat_data = coupledb.get(cid, {})
    image = chat_data.get("img", "")
    return image


async def get_couple(cid: int, date: str):
    lovers = await _get_lovers(cid)
    return lovers.get(date, False)


async def save_couple(cid: int, date: str, couple: dict, img: str):
    if cid not in coupledb:
        coupledb[cid] = {"off": {}, "img": ""}
    coupledb[cid]["off"][date] = couple
    coupledb[cid]["img"] = img


# ❤️ Love From KAIxGen
