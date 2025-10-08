import geopandas
import matplotlib.pyplot as plt
import requests
import os

# GeoJSON 文件的 URL
geojson_url = "https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json"
# 本地保存的文件名
file_path = "china_full.json"
# 希望保存的地图文件名 (PNG格式支持透明度)
output_filename = "china_map_transparent.png"

try:
    print(f"正在下载中国地图数据从 {geojson_url}...")
    response = requests.get(geojson_url)
    response.raise_for_status()

    with open(file_path, 'wb') as f:
        f.write(response.content)
    print(f"地图数据已保存到 {file_path}")

    print("正在加载地图数据...")
    china_map = geopandas.read_file(file_path)
    
    if china_map.empty:
        print("错误：加载的地图数据为空！请检查 GeoJSON 文件或 URL。")
        # exit()
    else:
        print("地图数据加载成功且不为空。")
        # 以下诊断信息可以帮助确认数据是否正确，如果确认无误可以注释掉
        # print(f"地图数据的坐标参考系统 (CRS): {china_map.crs}")
        # print(f"地图数据的总边界范围 (minx, miny, maxx, maxy): {china_map.total_bounds}")

    # 创建图形和坐标轴
    # figsize可以根据需要调整，它会影响最终图像中线条的相对粗细和整体大小
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))

    # --- 如果需要在matplotlib窗口预览时也看到透明背景（非必须，savefig的transparent=True更关键）---
    # fig.patch.set_alpha(0.0)  # 设置Figure的背景透明
    # ax.patch.set_alpha(0.0)   # 设置Axes的背景透明

    print("正在绘制地图 (仅边界线)...")
    # 绘制地图，确保区域内部无填充，只绘制黑色边界线
    china_map.plot(ax=ax,
                   edgecolor='black',  # 边界线颜色
                   facecolor='none',   # 区域内部不填充任何颜色
                   linewidth=1.5)     # 边界线宽度，您可以按需调整 (例如 1.0, 1.5, 2.0)

    # 移除坐标轴的所有元素（刻度、标签、边框线）
    ax.set_axis_off()

    print(f"准备将地图保存为具有透明背景的 {output_filename}...")
    # 保存图形到当前目录
    # transparent=True 是关键，它会使图表的背景透明
    # bbox_inches='tight' 会裁剪掉图像周围多余的空白（或透明）区域
    # dpi=300 设置图像的分辨率
    plt.savefig(output_filename,
                transparent=True,
                bbox_inches='tight',
                dpi=300)
    
    print(f"地图已成功保存为具有透明背景的文件: {os.path.join(os.getcwd(), output_filename)}")
    print("注意：查看PNG文件时，请使用支持显示透明背景的图像查看器或软件（如GIMP, Photoshop, 或在网页上设置背景色），否则透明区域可能会显示为查看器的默认背景色（如白色）。")

    # 关闭图形对象，释放内存
    plt.close(fig)

except requests.exceptions.RequestException as e:
    print(f"下载地图数据失败: {e}")
except FileNotFoundError:
    print(f"错误：无法找到文件 {file_path}。请确保下载步骤成功。")
except Exception as e:
    print(f"绘制或保存地图时发生错误: {e}")
    print("请确保您已正确安装 geopandas, matplotlib, 和 requests 库。")
finally:
    # 可选：在使用后删除下载的 GeoJSON 文件
    # if os.path.exists(file_path):
    #     os.remove(file_path)
    #     print(f"已删除临时文件 {file_path}")
    pass