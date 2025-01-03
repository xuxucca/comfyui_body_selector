import os
import sys
import json

# 确保当前目录在 Python 路径中
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

class BodyPartSelector:
    @classmethod
    def INPUT_TYPES(s):
        # 加载自定义词语
        custom_words = s.load_custom_words().get("body_parts", {})
        
        # 合并默认选项和自定义选项
        head_options = ["无", "头发", "刘海", "发型"] + list(custom_words.get("头部", {}).keys())
        face_options = ["无", "眼睛", "鼻子", "嘴巴", "耳朵", "眉毛", "睫毛", "脸颊", "下巴"] + list(custom_words.get("面部", {}).keys())
        hand_options = ["无", "手掌", "手指", "手腕", "指甲"] + list(custom_words.get("手部", {}).keys())
        leg_options = ["无", "大腿", "小腿", "脚踝", "脚"] + list(custom_words.get("腿部", {}).keys())
        torso_options = ["无", "胸部", "腰部", "肩膀", "手臂", "背部"] + list(custom_words.get("躯干", {}).keys())
        full_body_options = ["无", "全身"] + list(custom_words.get("全身", {}).keys())

        return {
            "required": {
                "头部": (head_options,),
                "面部": (face_options,),
                "手部": (hand_options,),
                "腿部": (leg_options,),
                "躯干": (torso_options,),
                "全身": (full_body_options,),
                "自定义词语": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "输入自定义词语(英文)"
                }),
            }
        }

    @classmethod
    def load_custom_words(cls):
        json_path = os.path.join(os.path.dirname(__file__), "custom_words.json")
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Warning: Could not load custom words: {e}")
            return {}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_prompt"
    CATEGORY = "prompt/body"

    # 中英文映射字典
    BODY_PARTS_MAP = {
        # 头部
        "头发": "hair",
        "刘海": "bangs",
        "发型": "hairstyle",
        # 面部
        "眼睛": "eyes",
        "鼻子": "nose",
        "嘴巴": "mouth",
        "耳朵": "ears",
        "眉毛": "eyebrows",
        "睫毛": "eyelashes",
        "脸颊": "cheeks",
        "下巴": "chin",
        # 手部
        "手掌": "palm",
        "手指": "fingers",
        "手腕": "wrist",
        "指甲": "nails",
        # 腿部
        "大腿": "thighs",
        "小腿": "calves",
        "脚踝": "ankles",
        "脚": "feet",
        # 躯干
        "胸部": "chest",
        "腰部": "waist",
        "肩膀": "shoulders",
        "手臂": "arms",
        "背部": "back",
        # 全身
        "全身": "full body"
    }

    def generate_prompt(self, 头部, 面部, 手部, 腿部, 躯干, 全身, 自定义词语):
        results = []
        custom_words = self.load_custom_words().get("body_parts", {})
        
        # 检查每个部位的选择
        for part, selection in [
            (头部, "头部"), (面部, "面部"), (手部, "手部"),
            (腿部, "腿部"), (躯干, "躯干"), (全身, "全身")
        ]:
            if part != "无":
                if part in self.BODY_PARTS_MAP:
                    results.append(self.BODY_PARTS_MAP[part])
                elif part in custom_words.get(selection, {}):
                    results.append(custom_words[selection][part])
        
        if 自定义词语.strip():
            results.append(自定义词语.strip())
        
        return (", ".join(results),)

class ClothingSelector:
    @classmethod
    def INPUT_TYPES(s):
        # 加载自定义词语
        custom_words = s.load_custom_words().get("clothing", {})
        
        # 合并默认选项和自定义选项
        tops_options = ["无", "T恤", "衬衫", "毛衣", "外套", "夹克"] + list(custom_words.get("上衣", {}).keys())
        pants_options = ["无", "牛仔裤", "短裤", "运动裤", "西装裤"] + list(custom_words.get("裤子", {}).keys())
        skirt_options = ["无", "短裙", "长裙", "百褶裙", "连衣裙"] + list(custom_words.get("裙子", {}).keys())
        shoe_options = ["无", "运动鞋", "高跟鞋", "靴子", "凉鞋"] + list(custom_words.get("鞋子", {}).keys())
        accessory_options = ["无", "帽子", "围巾", "手套", "袜子"] + list(custom_words.get("配饰", {}).keys())

        return {
            "required": {
                "上衣": (tops_options,),
                "裤子": (pants_options,),
                "裙子": (skirt_options,),
                "鞋子": (shoe_options,),
                "配饰": (accessory_options,),
                "自定义词语": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "输入自定义词语(英文)"
                }),
            }
        }

    @classmethod
    def load_custom_words(cls):
        json_path = os.path.join(os.path.dirname(__file__), "custom_words.json")
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Warning: Could not load custom words: {e}")
            return {}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_prompt"
    CATEGORY = "prompt/clothing"

    # 服装映射字典
    CLOTHING_MAP = {
        # 上衣
        "T恤": "t-shirt",
        "衬衫": "shirt",
        "毛衣": "sweater",
        "外套": "coat",
        "夹克": "jacket",
        # 裤子
        "牛仔裤": "jeans",
        "短裤": "shorts",
        "运动裤": "sweatpants",
        "西装裤": "suit pants",
        # 裙子
        "短裙": "short skirt",
        "长裙": "long skirt",
        "百褶裙": "pleated skirt",
        "连衣裙": "dress",
        # 鞋子
        "运动鞋": "sneakers",
        "高跟鞋": "high heels",
        "靴子": "boots",
        "凉鞋": "sandals",
        # 配饰
        "帽子": "hat",
        "围巾": "scarf",
        "手套": "gloves",
        "袜子": "socks",
    }

    def generate_prompt(self, 上衣, 裤子, 裙子, 鞋子, 配饰, 自定义词语):
        results = []
        custom_words = self.load_custom_words().get("clothing", {})
        
        # 检查每个服装类型的选择
        for clothing, selection in [
            (上衣, "上衣"), (裤子, "裤子"), (裙子, "裙子"),
            (鞋子, "鞋子"), (配饰, "配饰")
        ]:
            if clothing != "无":
                if clothing in self.CLOTHING_MAP:
                    results.append(self.CLOTHING_MAP[clothing])
                elif clothing in custom_words.get(selection, {}):
                    results.append(custom_words[selection][clothing])
        
        if 自定义词语.strip():
            results.append(自定义词语.strip())
        
        return (", ".join(results),)

# 注册节点
NODE_CLASS_MAPPINGS = {
    "BodyPartSelector": BodyPartSelector,
    "ClothingSelector": ClothingSelector
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BodyPartSelector": "身体部位选择器",
    "ClothingSelector": "服装选择器"
} 