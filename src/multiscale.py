import numpy as np
import rasterio
from rasterio.warp import reproject, Resampling
from rasterio.transform import from_origin


def aggregate_multiscale_area_weighted(
        src_array,
        src_transform,
        src_crs,
        target_res_m=250.0,
        resampling_method=Resampling.average
):

    # 1. 计算目标网格的形状 (四舍五入向上取整，确保完全覆盖)
    src_height, src_width = src_array.shape
    # 获取源影像的左上角坐标
    left, top = src_transform.c, src_transform.f

    # 计算目标网格的行列数
    dst_width = int(np.ceil((src_width * src_transform.a) / target_res_m))
    dst_height = int(np.ceil((src_height * abs(src_transform.e)) / target_res_m))

    # 2. 构建目标网格的 transform
    dst_transform = from_origin(left, top, target_res_m, target_res_m)

    # 3. 初始化目标数组
    dst_array = np.full((dst_height, dst_width), np.nan, dtype=np.float32)

    # 4. 调用 rasterio.warp.reproject 进行面积加权重采样
    # reproject 会自动计算源像素与目标像素的重叠面积
    reproject(
        source=src_array,
        destination=dst_array,
        src_transform=src_transform,
        src_crs=src_crs,
        dst_transform=dst_transform,
        dst_crs=src_crs,
        resampling=resampling_method
    )

    return dst_array, dst_transform


# ==========================================
# 使用示例 (Examples)
# ==========================================
if __name__ == "__main__":
    fvc_30m = np.random.rand(100, 100)
    src_transform = from_origin(0, 3000, 30, 30)  # 假设原点 (0,3000), 30m分辨率
    src_crs = 'EPSG:32650'  # UTM Zone 50N

    fvc_250m, t_250m = aggregate_multiscale_area_weighted(
        fvc_30m, src_transform, src_crs,
        target_res_m=250.0,
        resampling_method=Resampling.average
    )
    print(f"Original shape: {fvc_30m.shape}")
    print(f"Aggregated shape: {fvc_250m.shape}")


