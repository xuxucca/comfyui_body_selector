# ComfyUI Body & Clothing Selector

一个强大的 ComfyUI 插件，用于快速选择和生成人体部位和服装的英文描述词语。提供中文界面，支持自定义词语映射。

## 功能特点

- 分为身体部位选择器和服装选择器两个独立节点
- 所有选项支持中文显示，输出标准英文词语
- 每个选项都可以单独开启/关闭
- 支持通过 JSON 文件自定义添加新词语
- 支持即时输入自定义词语

## 安装方法

1. 进入 ComfyUI 的 custom_nodes 目录
2. 创建或克隆本插件到该目录：
```bash
cd custom_nodes
git clone [仓库地址] comfyui_body_selector
```
3. 重启 ComfyUI

## 使用方法

### 身体部位选择器

1. 在节点列表中找到"身体部位选择器"
2. 可选择的部位类别：
   - 头部（头发、刘海等）
   - 面部（眼睛、鼻子等）
   - 手部（手掌、手指等）
   - 腿部（大腿、小腿等）
   - 躯干（胸部、腰部等）
   - 全身
3. 选择"无"表示不使用该部位
4. 可以在自定义词语框中直接输入额外的英文描述

### 服装选择器

1. 在节点列表中找到"服装选择器"
2. 可选择的服装类别：
   - 上衣（T恤、衬衫等）
   - 裤子（牛仔裤、短裤等）
   - 裙子（短裙、长裙等）
   - 鞋子（运动鞋、高跟鞋等）
   - 配饰（帽子、围巾等）
3. 选择"无"表示不使用该类型
4. 可以在自定义词语框中直接输入额外的英文描述

### 自定义词语

你可以通过编辑 `custom_words.json` 文件来添加自己的词语映射：

```json
{
    "body_parts": {
        "头部": {
            "长发": "long hair",
            "短发": "short hair"
        }
    },
    "clothing": {
        "上衣": {
            "连帽衫": "hoodie",
            "背心": "tank top"
        }
    }
}
```

添加新词语后需要重启 ComfyUI 才能生效。

## 输出格式

- 所有选中的选项将以英文输出
- 多个选项用逗号分隔
- 示例：`eyes, long hair, hoodie`

## 实用技巧

1. 组合使用
   - 可以同时使用多个部位或服装
   - 可以配合其他提示词节点使用

2. 快速选择
   - 使用"无"选项快速关闭不需要的部分
   - 使用自定义词语框添加临时词语

3. 自定义扩展
   - 根据需要在 custom_words.json 中添加常用词语
   - 可以为不同场景准备不同的 custom_words.json

## 常见问题

Q: 为什么我添加的自定义词语没有显示？
A: 请确保：
1. custom_words.json 格式正确
2. 已经重启 ComfyUI
3. 文件使用 UTF-8 编码保存

Q: 如何同时使用多个部位/服装？
A: 直接在不同的下拉菜单中选择需要的选项，插件会自动组合所有选中的选项。

## 版本历史

- v1.0.0: 初始发布
  - 支持身体部位和服装选择
  - 支持自定义词语映射
  - 支持即时输入自定义词语

## 许可证

MIT License

## 贡献指南

欢迎提交 Pull Request 来改进这个插件：
1. 添加更多预设词语
2. 改进用户界面
3. 添加新功能
4. 修复 bug

## 联系方式

如有问题或建议，请通过以下方式联系：
- GitHub Issues
<<<<<<< HEAD
- [你的联系方式] 
=======
- [你的联系方式] 
>>>>>>> 48a4fe401397d3d75838a173c907bfe4a42ce866
