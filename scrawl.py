"""
爬虫程序入口
"""

import core
import model
import settings


def get_communitylist(city):
    res = []
    for community in model.Community.select():
        if community.city == city:
            res.append(community.title)
    return res


if __name__ == "__main__":
    # 从设置中读取社区列表；only pinyin support
    regionlist = settings.REGIONLIST
    city = settings.CITY

    # model是数据库模型。
    model.database_init()

    """
    core是核心爬虫模块。
    """

    """
    根据行政区来爬虫在售房源信息， 返回regionlist里面所有在售房源信息。
    由于链家限制，仅支持爬前100页数据，可使用GetHouseByCommunitylist。
    """
    # core.GetHouseByRegionlist(city, regionlist)

    """
    获取行政区在租房源信息
    """
    # core.GetRentByRegionlist(city, regionlist)  # 获取在租房子信息

    """
    获取行政区内小区信息，可以只运行一次即可。
    """
    # Init,scrapy celllist and insert database; could run only 1st time
    core.GetCommunityByRegionlist(city, regionlist)  # 根据行政区列表获取小区信息

    """
    根据小区来爬虫成交房源信息，返回communitylist里面所有成交房源信息。
    部分数据无法显示因为这些数据仅在链家app显示
    """

    communitylist = get_communitylist(city)
    core.GetHouseByCommunitylist(city, communitylist)
    core.GetSellByCommunitylist(city, communitylist)    # 成交房源信息
