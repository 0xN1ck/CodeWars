import pandas as pd


def max_common(df_a, df_b):
    df_res = pd.DataFrame(columns=df_a.columns)
    if df_a.empty: df_res = df_a
    for column in df_a:
        if column in df_b.columns:
            df_res[column] = pd.concat([df_a[column], df_b[column]], axis=1).max(axis=1).to_frame(name=column)
        else:
            df_res[column] = df_a[column]
    return df_res


if __name__ == '__main__':
    df_a = pd.DataFrame(data=[[2.5, 2.0, 2.0], [2.0, 2.0, 2.0]], columns=list('ABC'))
    df_b = pd.DataFrame(data=[[1.0, 6.0, 7.0, 1.0], [8.5, 1.0, 9.0, 1.0]], columns=list('CBDE'))
    df_out = pd.DataFrame(data=[[2.5, 6.0, 2.0], [2.0, 2.0, 8.5]], columns=list('ABC'))
    max_common(df_a, df_b)