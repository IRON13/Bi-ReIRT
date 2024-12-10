
import pandas as pd
from collections import OrderedDict
import os

# 定义文件名列表
file_names = [
    "Amazon_All_Beauty_Res.txt",
    "Amazon_Digital_Music_Res.txt",
    "Amazon_Gift_Cards_Res.txt",
    "Amazon_Handmade_Products_Res.txt",
    "Amazon_Health_and_Personal_Care_Res.txt",
    "Amazon_Magazine_Subscriptions_Res.txt",
    "Amazon_Subscription_Boxes_Res.txt",
    "ml-100k_Res.txt",
    "ml-1m_Res.txt",
    "epinions_Res.txt",
    "ModCloth_Res.txt"
]

# 定义需要的模型名称列表（并作为排序顺序）
required_models = [
    "Random",
    "Pop",
    "ItemKNN",
    "BPR",
    "ENMF",
    "DMF",
    "NNCF",
    "MultiDAE",
    "MultiVAE",
    "NCEPLRec",
    "RecVAE",
    "CDAE",
    "LINE",
    "SGL",
    "DiffRec",
    "RaCT",
    "SimpleX"
]

# 定义输入文件夹路径和输出文件夹路径
input_folder = "./Res/"  # 替换为你的输入文件夹路径
output_folder = "./Res/"  # 替换为你的输出文件夹路径

# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 循环处理文件
for file_name in file_names:
    input_file_path = os.path.join(input_folder, file_name)
    output_file_path = os.path.join(output_folder, file_name.replace(".txt", ".xlsx"))

    # 读取文件内容
    with open(input_file_path, "r", encoding="utf-8") as file:
        file_content = file.read()

    # 解析内容以提取模型名称和测试结果
    lines = file_content.strip().split("\n")
    models_data = []

    current_model = None
    for line in lines:
        if line.startswith("Model:"):
            current_model = line.split(":")[1].strip()
        elif line.startswith("test_result:") and current_model in required_models:
            test_result_data = eval(line.split(": ", 1)[1].strip(), {"OrderedDict": OrderedDict})
            for metric, value in test_result_data.items():
                models_data.append({"Model": current_model, metric: value})

    # 创建 DataFrame 并重塑结构
    df = pd.DataFrame(models_data)
    if not df.empty:
        df_grouped = df.groupby("Model").first().reset_index()

        # 按 required_models 的顺序排序
        df_grouped["Model"] = pd.Categorical(df_grouped["Model"], categories=required_models, ordered=True)
        df_sorted = df_grouped.sort_values("Model").reset_index(drop=True)

        # 保存为 Excel 文件
        df_sorted.to_excel(output_file_path, index=False)
        print(f"筛选并排序后的数据已保存到 {output_file_path}")
    else:
        print(f"文件 {file_name} 中没有匹配的模型数据，跳过保存")

