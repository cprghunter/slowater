import pandas as p
import sys

FNAME = "Water_Purveyors.csv"

if __name__ == "__main__":
    wpdf = p.read_csv(FNAME, index_col=0)
    total_purveyors = len(wpdf.index)
    total_pop_served = sum(p.to_numeric(wpdf["Pop_Served"], errors='coerce').fillna(0))
    print(total_pop_served)
    rows = wpdf.loc[wpdf['Level_'] == 'vulnerable']
    rows.append(wpdf.loc[wpdf['Level_'] == 'critical'])
    pending_rows = wpdf.loc[wpdf['Level_'] == 'pending']
    pop_in_danager = sum(p.to_numeric(rows["Pop_Served"], errors='coerce'))
    print(f"ratio of vuln/crit pop served: {pop_in_danager/total_pop_served}")
    print(len(rows.index)/total_purveyors)
    print(len(pending_rows.index)/total_purveyors)
