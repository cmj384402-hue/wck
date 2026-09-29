# wck — Codex 科研入门仓库

这是一个用于学习 **Codex + GitHub 辅助科研工作流** 的练习仓库。目标不是搭建复杂软件工程项目，而是建立一套清晰、可复用、适合科研数据分析与论文工作的目录结构。

## 目录结构

```text
wck/
├── README.md                 # 项目说明
├── .gitignore                # 忽略缓存、环境、临时输出等
├── requirements.txt          # 常用科研 Python 依赖
├── data/
│   ├── raw/                  # 原始数据：原则上只读，不直接修改
│   └── processed/            # 清洗、转换后的数据
├── scripts/
│   ├── README.md             # 脚本目录说明
│   └── example_analysis.py   # 最小数据分析示例
├── notebooks/
│   └── README.md             # Jupyter Notebook 使用规范
├── results/
│   └── README.md             # 图表、表格与分析结果
└── docs/
    └── README.md             # 实验记录、方法说明、论文草稿等
```

## 推荐科研工作流

1. 将原始实验数据放入 `data/raw/`。
2. 使用 Codex 编写或修改 `scripts/` 中的分析脚本。
3. 将清洗后的数据输出到 `data/processed/`。
4. 将图、表及中间结果输出到 `results/`。
5. 将分析逻辑、实验说明和论文相关材料整理到 `docs/`。
6. 每完成一个明确阶段，用 Git 提交一次版本。
7. 需要大改时新建分支，再通过 Pull Request 合并。

## Codex 练习任务

可以从下面几个任务开始：

- 读取 CSV/Excel 数据并检查缺失值；
- 计算均值、标准差及误差；
- 绘制科研常用折线图、散点图和柱状图；
- 批量重命名文件；
- 将重复的数据处理步骤封装成函数；
- 自动生成结果表；
- 根据修改要求创建分支、提交 commit 并建立 Pull Request。

## Python 环境

建议使用 Python 3.11 或更高版本。

安装依赖：

```bash
pip install -r requirements.txt
```

运行示例：

```bash
python scripts/example_analysis.py
```

## 版本管理建议

推荐采用以下提交习惯：

```text
feat: add adsorption data processing
fix: correct unit conversion
plot: update Figure 2 formatting
docs: revise analysis notes
data: add processed dataset
```

科研项目中建议避免把超大原始数据、临时文件、软件缓存和本地虚拟环境直接提交到 GitHub。

## 基本原则

- **raw data 保持原始状态**：不要覆盖原始实验数据。
- **处理过程可追溯**：尽量通过脚本生成 processed data 和 figures。
- **一次提交只完成一类修改**：便于回溯和比较。
- **代码、数据、结果分开存放**：降低后期整理成本。
- **重要结论写入文档**：不要只依赖聊天记录。

后续可以继续在这个仓库中练习 Codex 的读取文件、修改代码、运行分析、创建分支、提交 commit 和 Pull Request 等完整科研工作流。
