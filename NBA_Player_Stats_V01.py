# -*- coding: utf-8 -*-
"""
Created on 05/13, 2023
@author: WillyF

"""
# https://data.world/etocco/nba-player-stats
# https://www.basketball-reference.com/leagues/NBA_1997_per_game.html
# https://www.statscrew.com/basketball/t-WSB


from UI_V01 import *
import pandas as pd
import urllib.request


# import json
# import numpy as np
# from datetime import datetime

# import ssl
#
# ssl._create_default_https_context = ssl._create_unverified_context


# import warnings
# warnings.filterwarnings("ignore")
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.max_rows', 1000)


def Data_ETL():
    stats_append_1996_97 = pd.read_csv(
        'https://raw.githubusercontent.com/LeBronWilly/NBA_Player_Stats/main/1996-97_Stats_Append.txt').fillna(
        0.000).drop(columns=["Player-additional"])
    stats_append_1996_97["Season"] = "1996-97"
    stats_append_1996_97["MVP"] = False
    stats_append_1996_97.loc[stats_append_1996_97["Player"].str.contains("Karl Malone", regex=False), "MVP"] = True

    stats_append_2022_23 = pd.read_csv(
        'https://raw.githubusercontent.com/LeBronWilly/NBA_Player_Stats/main/2022-23_Stats_Append.txt').fillna(
        0.000).drop(columns=["Player-additional"])
    stats_append_2022_23["Season"] = "2022-23"
    stats_append_2022_23["MVP"] = False
    stats_append_2022_23.loc[stats_append_2022_23["Player"].str.contains("Joel Embiid", regex=False), "MVP"] = True

    nba_team_list = pd.read_csv(
        'https://raw.githubusercontent.com/LeBronWilly/NBA_Player_Stats/main/NBA_Team_List.csv').fillna(0.000)
    nba_player_df = pd.read_csv('https://query.data.world/s/ty4piswbrsp54noyh2bdvrjecv24ta?dws=00000').fillna(0.000)
    nba_player_df = pd.concat([nba_player_df, stats_append_1996_97, stats_append_2022_23], ignore_index=True)
    nba_player_df["BHOF"] = False
    nba_player_df.loc[nba_player_df["Player"].str.contains("*", regex=False), "BHOF"] = True
    nba_player_df["Player"] = nba_player_df["Player"].str.strip("*")
    nba_player_df = nba_player_df.merge(nba_team_list, how="left", on="Tm", validate="many_to_one").drop(columns=["Rk"])
    nba_player_df = nba_player_df.sort_values(by=['Season', 'Player']).reset_index(drop=True)
    nba_player_df.insert(3, 'Season', nba_player_df.pop('Season'))
    nba_player_df.insert(4, 'Team', nba_player_df.pop('Team'))
    nba_player_df.insert(5, 'Season_MVP', nba_player_df.pop('MVP'))
    nba_player_df.insert(6, 'BHOF', nba_player_df.pop('BHOF'))
    nba_player_df.insert(len(nba_player_df.columns) - 1, 'Tm', nba_player_df.pop('Tm'))
    return nba_player_df


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NBA_Player_Stats()
        self.ui.setupUi(self)
        print("Loading NBA Player Stats Data......")
        self.Stats_data = None
        self.setup_control()
        print("Done!")
        self.show()

    def setup_control(self):
        # self.ui.WinIcon_img = QPixmap()
        # url = 'https://raw.githubusercontent.com/LeBronWilly/TW_Weather_FCST/main/weather-forecast.png'
        # img_data = urllib.request.urlopen(url).read()
        # self.ui.WinIcon_img.loadFromData(img_data)
        # self.ui.WinIcon_img = self.ui.WinIcon_img.scaled(75, 75)
        # self.setWindowIcon(QIcon(self.ui.WinIcon_img))
        # self.ui.Pic_Label.setPixmap(self.ui.WinIcon_img)
        # self.ui.Pic_Label.setAlignment(Qt.AlignCenter)
        self.ui.Info_Table.clear()
        self.ui.Info_Table.setColumnCount(0)
        self.ui.Info_Table.setRowCount(0)
        # self.ui.Field_Desc_Table.resizeColumnsToContents()
        # self.ui.Field_Desc_Table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.Stats_data = Data_ETL()
        self.ui.Player_ComboBox.clear()
        self.ui.Player_ComboBox.addItem("[All Players]")
        self.ui.player_list = sorted(set(self.Stats_data["Player"]))
        for player in self.ui.player_list:
            self.ui.Player_ComboBox.addItem(player)
        self.ui.Team_ComboBox.clear()
        self.ui.Team_ComboBox.addItem("[All Teams]")
        self.ui.team_list = sorted(set(self.Stats_data["Team"]))
        for team in self.ui.team_list:
            self.ui.Team_ComboBox.addItem(team)
        self.ui.Season_ComboBox.clear()
        self.ui.Season_ComboBox.addItem("[All Seasons]")
        self.ui.season_list = sorted(set(self.Stats_data["Season"]))
        for season in self.ui.season_list:
            self.ui.Season_ComboBox.addItem(season)

        self.ui.Refresh_Button.clicked.connect(self.Refresh_Button_Clicked)
        # self.ui.Search_Button.clicked.connect(
        #     lambda: self.Search_Button_Clicked(self.ui.Season_ComboBox.currentText(),
        #                                        self.ui.Player_ComboBox.currentText()))
        # self.ui.Team_ComboBox.currentTextChanged.connect(
        #     lambda: self.Region_Change(self.ui.Team_ComboBox.currentText()))

        # self.ui.Update_Time_Label.setText("Data Last Updated: " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

    def Region_Change(self, Region_Name):
        return
        # if Region_Name is None:
        #     return None
        # if Region_Name == "所有地區 (北/中/南/東/外島)":
        #     current_loc = self.ui.Location_ComboBox.currentText()
        #     self.ui.Location_ComboBox.clear()
        #     self.ui.loc_list = sorted(set(self.FCST_data["Location"]))
        #     for loc in self.ui.loc_list:
        #         self.ui.Location_ComboBox.addItem(loc)
        #     self.ui.Location_ComboBox.setCurrentText(current_loc)
        # else:
        #     df_table = self.FCST_data.copy()
        #     df_table = df_table[df_table["Region"] == Region_Name]
        #     self.ui.Location_ComboBox.clear()
        #     self.ui.loc_list = sorted(set(df_table["Location"]))
        #     for loc in self.ui.loc_list:
        #         self.ui.Location_ComboBox.addItem(loc)

    def Refresh_Button_Clicked(self):
        print("Loading NBA Player Stats Data......")
        self.ui.Info_Table.clear()
        self.ui.Info_Table.setColumnCount(0)
        self.ui.Info_Table.setRowCount(0)
        self.Stats_data = Data_ETL()
        self.ui.Player_ComboBox.clear()
        self.ui.Player_ComboBox.addItem("[All Players]")
        self.ui.player_list = sorted(set(self.Stats_data["Player"]))
        for player in self.ui.player_list:
            self.ui.Player_ComboBox.addItem(player)
        self.ui.Team_ComboBox.clear()
        self.ui.Team_ComboBox.addItem("[All Teams]")
        self.ui.team_list = sorted(set(self.Stats_data["Team"]))
        for team in self.ui.team_list:
            self.ui.Team_ComboBox.addItem(team)
        self.ui.Season_ComboBox.clear()
        self.ui.Season_ComboBox.addItem("[All Seasons]")
        self.ui.season_list = sorted(set(self.Stats_data["Season"]))
        for season in self.ui.season_list:
            self.ui.Season_ComboBox.addItem(season)
        # self.ui.Update_Time_Label.setText("Data Last Updated: " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
        print("Done!")

    def Search_Button_Clicked(self, LocationName, PeriodName):
        return
        # self.ui.Info_Table.clear()
        # df_table = self.FCST_data.copy()[["Period", "Region", "Location", "Weather FCST", "12hr PoP", "T",
        #                                   "AvgT", "AT", "AvgRH", "AvgDPT", "UVI", "MaxWS", "BWS", "WD", "CI"]]
        # if PeriodName == "所有期間":
        #     PeriodName = ""
        # df_table = df_table[(df_table["Location"] == LocationName)]
        # df_table = df_table[(df_table["Period"].str.contains(PeriodName.split(" ")[0], regex=False))]
        # df_table_nrows = df_table.shape[0]
        # df_table_ncolumns = df_table.shape[1]
        # df_table_columns_names = df_table.columns
        # self.ui.Info_Table.setColumnCount(df_table_ncolumns)
        # self.ui.Info_Table.setRowCount(df_table_nrows)
        # self.ui.Info_Table.setHorizontalHeaderLabels(df_table_columns_names)
        # for i in range(0, df_table_nrows):
        #     df_table_row_values_list = list(df_table.iloc[i])
        #     self.ui.Info_Table.setRowHeight(i, 1)
        #     for j in range(0, df_table_ncolumns):
        #         df_table_values_item = str(df_table_row_values_list[j])
        #         new_item = QTableWidgetItem(df_table_values_item)
        #         new_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        #         self.ui.Info_Table.setItem(i, j, new_item)
        #         self.ui.Info_Table.horizontalHeader().setSectionResizeMode(j, QHeaderView.ResizeToContents)
        # print(LocationName, PeriodName)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    NBA_Player_Stats = AppWindow()
    NBA_Player_Stats.show()
    sys.exit(app.exec_())
    input("WillyF")