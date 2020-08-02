def backlimit():
    sql = """SELECT
        plantreal24.r_date AS datetime,
        plantreal24.fore24 AS fore24,
        plantreal24.tail24 AS tail24,
        plantreal24.tail24_avg AS tail24_avg,
        plantreal24.evap AS evap,
        plantreal24.infl AS infl,
        plantreal24.losses AS losses,
        plantreal24.rel1 AS rel1,
        plantreal24.rel2 AS rel2,
        plantreal24.rel3 AS rel3,
        plantreal24.rel_tol AS rel_tol,
        plantreal24.engr1 AS engr1,
        plantreal24.engr2 AS engr2,
        plantreal24.engr3 AS engr3,
        plantreal24.cond1 AS cond1,
        plantreal24.cond2 AS cond2,
        plantreal24.cond3 AS cond3,
        plantreal24.str1 AS str1,
        plantreal24.str2 AS str2,
        plantreal24.str3 AS str3,
        plantreal24.run_g1 AS run_g1,
        plantreal24.run_g2 AS run_g2,
        plantreal24.run_g3 AS run_g3,
        plantreal24.run_c1 AS run_c1,
        plantreal24.run_c2 AS run_c2,
        plantreal24.run_c3 AS run_c3,
        plantreal24.spillway AS spillway,
        plantreal24.irr AS irr,
        plantreal24.camp AS camp,
        plantreal24.demand AS demand,
        plantreal24.derate AS derate,
        plantreal24.outage AS outage,
        plantreal24.stor
        FROM
        plantreal24
        ORDER BY
        datetime DESC
    """
    return sql

def backlast():
    sql = """SELECT
        plantreal24.r_date AS datetime,
        plantreal24.fore24 AS fore24,
        plantreal24.tail24 AS tail24,
        plantreal24.tail24_avg AS tail24_avg,
        plantreal24.evap AS evap,
        plantreal24.infl AS infl,
        plantreal24.losses AS losses,
        plantreal24.rel1 AS rel1,
        plantreal24.rel2 AS rel2,
        plantreal24.rel3 AS rel3,
        plantreal24.rel_tol AS rel_tol,
        plantreal24.engr1 AS engr1,
        plantreal24.engr2 AS engr2,
        plantreal24.engr3 AS engr3,
        plantreal24.cond1 AS cond1,
        plantreal24.cond2 AS cond2,
        plantreal24.cond3 AS cond3,
        plantreal24.str1 AS str1,
        plantreal24.str2 AS str2,
        plantreal24.str3 AS str3,
        plantreal24.run_g1 AS run_g1,
        plantreal24.run_g2 AS run_g2,
        plantreal24.run_g3 AS run_g3,
        plantreal24.run_c1 AS run_c1,
        plantreal24.run_c2 AS run_c2,
        plantreal24.run_c3 AS run_c3,
        plantreal24.spillway AS spillway,
        plantreal24.irr AS irr,
        plantreal24.camp AS camp,
        plantreal24.demand AS demand,
        plantreal24.derate AS derate,
        plantreal24.outage AS outage,
        plantreal24.stor
        FROM
        plantreal24
        ORDER BY
        datetime DESC
        limit %s
    """
    return sql
