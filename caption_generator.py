import json

def get_caption(product, style):
    if style == "hype":
        caption = f"New drop alret! our {product} is here"
    elif style == "classy" :
        caption = f"introducing our new product {product}"
    elif style == "minimal":
        caption = f"{product} is available now"
    else:
        caption = f"new drop {product}"
    return caption


def saved_caption(caption):
    try:
        with open("captions.json", "r") as file:
            saved_captions = json.load(file)
    except FileNotFoundError:
        saved_captions = []
    saved_captions.append(caption)     # ← add this before the save block

    with open("captions.json", "w") as file:
        json.dump(saved_captions,file)
    print(f"\n saved! you now have {len(saved_captions)} is your libray")



product = input("what product are you posting?")
style = input("pick a style (hype/classy/minimal)")
hashtags = "#sml#shoes"


caption = get_caption(product,style)
print("\n" + caption)
print(hashtags)


saved_caption(caption)