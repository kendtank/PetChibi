# -*- coding: utf-8 -*-
"""
@Time    : 2026/5/19 10:27
@Author  : Kend
@FileName: replicate-token
@Software: PyCharm
@modifier:
"""


import replicate

output = replicate.run(
    "black-forest-labs/flux-kontext-pro",
    input={

        # 刀疤猫咪图 URL
        # "input_image": "https://github.com/kendtank/PetChibi/blob/main/daoba_cat.jpg",

        # 嘟嘟照片
        "input_image": "https://raw.githubusercontent.com/kendtank/PetChibi/main/dudu_dog.jpg",

        # Prompt
        "prompt": """
        Transform this dog into an ultra cute chibi pet avatar.

        Keep the identity of the original dog:
        - white Bichon Frise
        - fluffy curly white fur
        - small compact body
        - round face
        
        Style:
        - chibi proportions (large head, small body)
        - Pixar / Disney 3D style
        - Pop Mart blind box collectible toy
        - soft plush toy texture
        - extremely fluffy curly fur
        - big sparkling eyes
        - adorable innocent expression
        - premium vinyl toy look
        - soft cinematic lighting
        - high quality 3D render
        
        Make it extremely cute and emotionally appealing.
        Maximize cuteness and toy-like appearance.
        """,


        "aspect_ratio": "match_input_image",

        "output_format": "jpg",

        "safety_tolerance": 2,

        "prompt_upsampling": False
    }
)

# 输出 URL
print(output.url)

# 保存到本地
with open("pet_chibi_dudu_result.jpg", "wb") as file:
    file.write(output.read())

print("生成完成")




