from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Pie, Page


def visualization(list1):
    work_experience, education, company_type, company_size = {}, {}, {}, {}
    for i in list1:
        if i[3] not in work_experience:
            work_experience[i[3]] = 1
        else:
            work_experience[i[3]] += 1
        if i[4] not in education:
            education[i[4]] = 1
        else:
            education[i[4]] += 1
        if i[8] not in company_type:
            company_type[i[8]] = 1
        else:
            company_type[i[8]] += 1
        if i[9] not in company_size:
            company_size[i[9]] = 1
        else:
            company_size[i[9]] += 1
    if None in list(work_experience.keys()):
        work_experience.pop(None)
    if None in list(education.keys()):
        education.pop(None)
    if None in list(company_size.keys()):
        company_size.pop(None)
    if None in list(company_type.keys()):
        company_type.pop(None)

    bar1 = Bar()
    bar1.add_xaxis(list(company_size.keys()))
    bar1.add_yaxis("个数", list(company_size.values()))
    bar1.set_global_opts(title_opts=opts.TitleOpts(title="公司规模"))

    pie1 = (Pie()
            .add("", list(zip(list(education.keys()), list(education.values()))), center=["25%", "50%"])
            .set_global_opts(title_opts=opts.TitleOpts(title="学历分布", pos_left='5%'),
                             legend_opts=opts.LegendOpts(pos_left="5%", pos_bottom="5%"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}\n{d}%"))
            )

    bar2 = Bar()
    bar2.add_xaxis(list(work_experience.keys()))
    bar2.add_yaxis("个数", list(work_experience.values()))
    bar2.set_global_opts(title_opts=opts.TitleOpts(title="工作经验分布"))

    pie2 = (Pie()
            .add("", list(zip(list(company_type.keys()), list(company_type.values()))), center=["75%", "50%"])
            .set_global_opts(title_opts=opts.TitleOpts(title="公司类型分布", pos_right='7%'),
                             legend_opts=opts.LegendOpts(pos_right="5%", pos_bottom="0%"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}\n{d}%"))
            )
    grid1_1 = Grid(init_opts=opts.InitOpts(width='1600px'))
    grid1_1.add(pie1, grid_opts=opts.GridOpts(pos_right="55%"))
    grid1_1.add(pie2, grid_opts=opts.GridOpts(pos_left="55%"))
    page_1 = Page(layout=Page.SimplePageLayout)
    page_1.add(bar1)
    page_1.add(grid1_1)
    page_1.add(bar2)

    return page_1