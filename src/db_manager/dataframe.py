import pandas as pd


class DataframeHandler:
    def __init__(self) -> None:
        pass

    def normalize_column_names(self, df:pd.DataFrame) -> pd.DataFrame:
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
        return df

