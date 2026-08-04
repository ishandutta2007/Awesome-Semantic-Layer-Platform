import re
import os
import subprocess

readme_path = r"C:\Users\ishan\Documents\Projects\Awesome-Semantic-Layer-Platform\README.md"
repo_path = r"C:\Users\ishan\Documents\Projects\Awesome-Semantic-Layer-Platform"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

def run_git(msg):
    subprocess.run(['git', '-C', repo_path, 'add', '.'])
    subprocess.run(['git', '-C', repo_path, 'commit', '-m', msg])
    subprocess.run(['git', '-c', 'http.sslVerify=false', '-C', repo_path, 'push'])

# 1. SaaS Products
# Replace the SaaS table
saas_table = """| Platform | Description | Pricing / Free Tier Limit | Company Size / Valuation |
| :--- | :--- | :--- | :--- |
| **Power BI Semantic Models** | Platform-native semantic modeling inside major BI and analytics tools. | Power BI Desktop is free; Pro starts at $10/user/mo. | ~$3T (Microsoft) |
| **Looker (LookML)** | Platform-native semantic modeling inside major BI and analytics tools. | Enterprise pricing (Contact Sales). | ~$2T (Google) |
| **[dbt Semantic Layer / MetricFlow](https://www.getdbt.com/product/semantic-layer)** | Metrics defined in dbt projects and served through dbt Cloud. | Free Developer tier (1 developer seat, 1 project); Paid starts at $100/mo. | ~$4.2B |
| **[Transform](https://transform.co/)** | Modern semantic modeling and metrics platform. | N/A (Acquired by dbt Labs). | ~$4.2B (dbt) |
| **[Cube](https://cube.dev/)** | Headless BI and semantic layer platform with strong API, caching, embedded analytics. | Free Developer tier (1 deployment, up to 1GB data passed); Paid starts at $99/mo. | ~$500M |
| **[AtScale](https://www.atscale.com/)** | Enterprise semantic / virtual OLAP layer with broad BI tool compatibility. | Enterprise pricing (Contact Sales). No free tier. | ~$500M |
| **[Hex Metrics](https://hex.tech)** | Platform-native semantic modeling inside major BI and analytics tools. | Community tier is free (up to 3 projects, 5 authors); Paid starts at $36/user/mo. | ~$300M |
| **[GoodData](https://www.gooddata.com/)** | Modern semantic modeling and metrics platform. | Free tier available (up to 5 workspaces); Paid starts at $1,500/mo. | ~$300M |
| **[Omni](https://omni.co/)** | Modern semantic modeling and metrics platform. | Custom pricing (Contact Sales). | ~$100M |
| **Kyvos** | Platform-native semantic modeling inside major BI and analytics tools. | Custom pricing (Contact Sales). | ~$50M |
| **Metric Insights** | Platform-native semantic modeling inside major BI and analytics tools. | Custom pricing (Contact Sales). | ~$50M |
| **[Honeydew](https://honeydew.ai/)** | Modern semantic modeling and metrics platform. | Custom pricing (Contact Sales). | ~$10M |"""

content = re.sub(r'\| Platform \| Description \| Pricing / Free Tier Limit \|\n\| :--- \| :--- \| :--- \|\n(?:\|.*?\|\n)+', saas_table + "\n", content)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)
run_git("Added company size and sorted the SaaS based on that")


# 2. Open-Source Repos
# Replacements for OSS stars
oss_old = """- **[Cube Core](https://github.com/cube-js/cube)** — The leading open-source (Apache 2.0) semantic layer and headless BI platform. Define metrics in YAML/JavaScript, serve them via SQL, REST, GraphQL, and more, with built-in caching and pre-aggregations. Fully self-hostable.
- **[MetricFlow](https://github.com/dbt-labs/metricflow)** — Open-source metrics engine developed by dbt Labs. Powers the dbt Semantic Layer and allows defining reusable metrics in YAML that compile to efficient SQL.
- **[Lightdash](https://github.com/lightdash/lightdash)** — Open-source BI tool that turns dbt models and metrics into a governed exploration experience. Excellent companion when you want an open-source consumption layer on top of dbt + MetricFlow.
- Emerging universal metrics runtimes (such as Sidemantic) that aim to import and serve models from multiple formats (Cube, MetricFlow, LookML, etc.)."""

oss_new = """- **[Cube Core](https://github.com/cube-js/cube)** [![GitHub stars](https://img.shields.io/github/stars/cube-js/cube?style=social&color=white)](https://github.com/cube-js/cube/stargazers) — The leading open-source (Apache 2.0) semantic layer and headless BI platform. Define metrics in YAML/JavaScript, serve them via SQL, REST, GraphQL, and more, with built-in caching and pre-aggregations. Fully self-hostable.
- **[Lightdash](https://github.com/lightdash/lightdash)** [![GitHub stars](https://img.shields.io/github/stars/lightdash/lightdash?style=social&color=white)](https://github.com/lightdash/lightdash/stargazers) — Open-source BI tool that turns dbt models and metrics into a governed exploration experience. Excellent companion when you want an open-source consumption layer on top of dbt + MetricFlow.
- **[MetricFlow](https://github.com/dbt-labs/metricflow)** [![GitHub stars](https://img.shields.io/github/stars/dbt-labs/metricflow?style=social&color=white)](https://github.com/dbt-labs/metricflow/stargazers) — Open-source metrics engine developed by dbt Labs. Powers the dbt Semantic Layer and allows defining reusable metrics in YAML that compile to efficient SQL.
- Emerging universal metrics runtimes (such as Sidemantic) that aim to import and serve models from multiple formats (Cube, MetricFlow, LookML, etc.)."""

content = content.replace(oss_old, oss_new)
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)
run_git("Added github stars and sorted the opensource based on that")


# 3. Decorate README banner
banner_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:rgb(131,58,180);stop-opacity:1" />
      <stop offset="50%" style="stop-color:rgb(253,29,29);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(252,176,69);stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="800" height="200" fill="url(#grad1)" rx="15" />
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="Arial, sans-serif" font-size="40" font-weight="bold" fill="white">Awesome Semantic Layer</text>
</svg>'''

assets_dir = os.path.join(repo_path, 'assets')
os.makedirs(assets_dir, exist_ok=True)
with open(os.path.join(assets_dir, 'banner.svg'), 'w', encoding='utf-8') as f:
    f.write(banner_svg)

content = "![Awesome Semantic Layer](assets/banner.svg)\n\n" + content
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)
run_git("added banner")


# 4. Decorate README with emojis
content = content.replace("## Similar Projects", "## 🔍 Similar Projects")
content = content.replace("### Core Open-Source", "### 🛠️ Core Open-Source")
content = content.replace("### Related Open-Source", "### 🔗 Related Open-Source")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)
run_git("added emojis")


# 5. Make the README more SEO-friendly
content = content.replace("# Awesome-Semantic-Layer-Platform", "# Awesome Semantic Layer Platform: A Curated List of Headless BI and Metrics Layers")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)
run_git("seo optimised")


# 6 & 7. Decorate README with badges
left_badges = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'
right_badges = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'

badge_line = f"<div align=\"center\">\n{left_badges} {right_badges}\n</div>\n\n"
content = content.replace("# Awesome Semantic Layer Platform", badge_line + "# Awesome Semantic Layer Platform")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)
run_git("badges to left added")
run_git("badges to right added")


# 8. Star History
star_history = """
## ⭐️ Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Semantic-Layer-Platform&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Semantic-Layer-Platform&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Semantic-Layer-Platform&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Semantic-Layer-Platform&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
content = content + star_history
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)
run_git("star history added")


# 9 & 10. Replace chartrepos and invalid awesome link
content = content.replace("chartrepos", "chart?repos")
content = content.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)
run_git("fixed star plot")
run_git("invalid awesome link fixed")
