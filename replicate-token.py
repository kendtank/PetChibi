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
        "input_image": "https://raw.githubusercontent.com/kendtank/PetChibi/main/daoba_cat.jpg",

        # Prompt
        "prompt": """
        Transform this Maine Coon cat into a stylized 3D collectible toy avatar.

        IMPORTANT:
        - Keep it as an adult Maine Coon cat
        - Do NOT turn it into a kitten
        - Preserve strong facial structure and mature proportions
        - Maintain original orange and white fur pattern
        
        Style:
        - subtle chibi stylization (not extreme)
        - Pixar-quality 3D render
        - premium vinyl collectible figure
        - soft cinematic lighting
        - high detail fur
        - realistic anatomy under stylization
        - cute but mature expression
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
with open("pet_chibi_daoba_result.jpg", "wb") as file:
    file.write(output.read())

print("生成完成")




