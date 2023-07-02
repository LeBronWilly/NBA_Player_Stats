# -*- coding: utf-8 -*-
"""
Created on 05/13, 2023
@author: WillyF

"""
# https://data.world/etocco/nba-player-stats
# https://www.basketball-reference.com/leagues/NBA_1997_per_game.html
# https://www.statscrew.com/basketball/t-WSB
# https://stackoverflow.com/questions/60522103/how-to-have-plotly-graph-as-pyqt5-widget
# https://stackoverflow.com/questions/52485735/how-do-i-display-a-border-around-a-qwebengineview


from UI_V02 import *
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
    nba_player_df["FG%"] = nba_player_df["FG%"].apply(lambda x: str(round(x * 100, 1)) + "%")
    nba_player_df["3P%"] = nba_player_df["3P%"].apply(lambda x: str(round(x * 100, 1)) + "%")
    nba_player_df["2P%"] = nba_player_df["2P%"].apply(lambda x: str(round(x * 100, 1)) + "%")
    nba_player_df["eFG%"] = nba_player_df["eFG%"].apply(lambda x: str(round(x * 100, 1)) + "%")
    nba_player_df["FT%"] = nba_player_df["FT%"].apply(lambda x: str(round(x * 100, 1)) + "%")
    nba_player_df["Year"] = nba_player_df["Season"].apply(lambda x: int(x[:4]))
    return nba_player_df


from PySide2 import QtWebEngineWidgets
import plotly.express as px


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NBA_Player_Stats()
        self.ui.setupUi(self)
        ######
        self.Chart_Plotly = QtWebEngineWidgets.QWebEngineView(self)
        self.Chart_Plotly.setGeometry(QRect(30, 565, 1221, 351))
        self.Chart_Plotly.setContentsMargins(1, 1, 1, 1)
        df = px.data.tips()
        fig = px.box(df, x="day", y="total_bill", color="smoker")
        fig.update_traces(quartilemethod="exclusive")  # or "inclusive", or "linear" by default
        df = pd.DataFrame(dict(
            x=[1, 2, 3, 4, 5],
            y=[1, 2, None, 4, 6],
        ))
        df = df.sort_values(by="x")
        fig = px.line(df, x="x", y="y", title="Unsorted Input")
        fig.update_traces(connectgaps=True)
        self.Chart_Plotly.setHtml(fig.to_html(include_plotlyjs='cdn'))
        ######
        print("Loading NBA Player Stats Data......")
        self.Stats_data_source = Data_ETL()
        print("Done!")
        self.setup_control()
        self.show()

    def setup_control(self):
        self.ui.WinIcon_img = QPixmap()
        url = 'https://raw.githubusercontent.com/LeBronWilly/NBA_Player_Stats/main/icon2.png'
        img_data = urllib.request.urlopen(url).read()
        self.ui.WinIcon_img.loadFromData(img_data)
        # self.ui.WinIcon_img = self.ui.WinIcon_img.scaled(75, 75)
        self.setWindowIcon(QIcon(self.ui.WinIcon_img))

        self.ui.Icon_img = QPixmap()
        url = 'https://raw.githubusercontent.com/LeBronWilly/NBA_Player_Stats/main/nba_logo.png'
        img_data = urllib.request.urlopen(url).read()
        self.ui.Icon_img.loadFromData(img_data)
        # self.ui.Icon_img = self.ui.Icon_img.scaled(125, 75)
        self.ui.Pic_Label.setPixmap(self.ui.Icon_img)
        self.ui.Pic_Label.setAlignment(Qt.AlignCenter)
        self.ui.Pic_Label.setScaledContents(True)  # 圖片就不會失真

        self.ui.Info_Table.clear()
        self.ui.Info_Table.setColumnCount(0)
        self.ui.Info_Table.setRowCount(0)
        # self.ui.Field_Desc_Table.resizeColumnsToContents()
        # self.ui.Field_Desc_Table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.Player_ComboBox.clear()
        self.ui.Player_ComboBox.addItem("All Players")
        self.ui.player_list = sorted(set(self.Stats_data_source["Player"]))
        for player in self.ui.player_list:
            self.ui.Player_ComboBox.addItem(player)

        self.ui.Team_Filter_ComboBox.clear()
        self.ui.Team_Filter_ComboBox.addItem("All Teams")
        self.ui.Team_ComboBox.clear()
        self.ui.Team_ComboBox.addItem("All Teams")
        self.ui.team_list = sorted(set(self.Stats_data_source["Team"]))
        for team in self.ui.team_list:
            if team != "Two Other Teams":
                self.ui.Team_Filter_ComboBox.addItem(team)
                self.ui.Team_ComboBox.addItem(team)

        self.ui.Season_Filter_ComboBox.clear()
        self.ui.Season_Filter_ComboBox.addItem("All Seasons")
        self.ui.Season_ComboBox.clear()
        self.ui.Season_ComboBox.addItem("All Seasons")
        self.ui.season_list = sorted(set(self.Stats_data_source["Season"]))
        for season in self.ui.season_list:
            self.ui.Season_Filter_ComboBox.addItem(season)
            self.ui.Season_ComboBox.addItem(season)

        self.ui.KeyWord_Text.clear()
        self.ui.Reset_Button.clicked.connect(self.Reset_Button_Clicked)
        self.ui.KeyWord_Text.textChanged.connect(
            lambda: self.Filter_Change(self.ui.KeyWord_Text.text().strip(),
                                       self.ui.Team_Filter_ComboBox.currentText(),
                                       self.ui.Season_Filter_ComboBox.currentText()))
        self.ui.Team_Filter_ComboBox.currentTextChanged.connect(
            lambda: self.Filter_Change(self.ui.KeyWord_Text.text().strip(),
                                       self.ui.Team_Filter_ComboBox.currentText(),
                                       self.ui.Season_Filter_ComboBox.currentText()))
        self.ui.Season_Filter_ComboBox.currentTextChanged.connect(
            lambda: self.Filter_Change(self.ui.KeyWord_Text.text().strip(),
                                       self.ui.Team_Filter_ComboBox.currentText(),
                                       self.ui.Season_Filter_ComboBox.currentText()))
        self.ui.Player_ComboBox.currentTextChanged.connect(
            lambda: self.Player_Change(self.ui.Player_ComboBox.currentText()))
        self.ui.Search_Button.clicked.connect(
            lambda: self.Search_Button_Clicked(self.ui.Player_ComboBox.currentText(),
                                               self.ui.Team_ComboBox.currentText(),
                                               self.ui.Season_ComboBox.currentText()))

        # self.ui.Player_ComboBox.setCurrentText("LeBron James")  # 初始預設LBJ
        # self.Search_Button_Clicked(self.ui.Player_ComboBox.currentText(),
        #                            self.ui.Team_ComboBox.currentText(),
        #                            self.ui.Season_ComboBox.currentText())

    def Filter_Change(self, Player_Name_Keyword, Player_Team, Player_Season):
        Player_Team_tmp = Player_Team
        Player_Season_tmp = Player_Season
        if Player_Team is None or Player_Season is None:
            return None
        if Player_Team == "All Teams":
            Player_Team_tmp = ""
        if Player_Season == "All Seasons":
            Player_Season_tmp = ""
        # print(Player_Name_Keyword is None)
        # print(Player_Name_Keyword, Player_Team_tmp, Player_Season_tmp)
        Stats_data_tmp = self.Stats_data_source.copy()
        Stats_data_tmp = Stats_data_tmp[Stats_data_tmp["Team"].str.contains(Player_Team_tmp, regex=False)]
        Stats_data_tmp = Stats_data_tmp[Stats_data_tmp["Season"].str.contains(Player_Season_tmp, regex=False)]
        Stats_data_tmp = Stats_data_tmp[
            Stats_data_tmp["Player"].str.contains(Player_Name_Keyword, regex=False, case=False)]
        # if Player_Name_Keyword != "" or Player_Name_Keyword == "":
        #     Stats_data_tmp = Stats_data_tmp[
        #         Stats_data_tmp["Player"].str.contains(Player_Name_Keyword, regex=False, case=False)]
        # else:
        #     return None

        self.ui.Player_ComboBox.clear()
        self.ui.Player_ComboBox.addItem("All Players")
        self.ui.player_list = sorted(set(Stats_data_tmp["Player"]))
        for player in self.ui.player_list:
            self.ui.Player_ComboBox.addItem(player)

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

    def Player_Change(self, PlayerName):
        PlayerName_tmp = PlayerName
        if PlayerName is None:
            return None
        if PlayerName == "All Players":
            PlayerName_tmp = ""

        Stats_data_tmp = self.Stats_data_source.copy()
        if PlayerName_tmp != "" or PlayerName_tmp == "":
            Stats_data_tmp = Stats_data_tmp[
                Stats_data_tmp["Player"].str.contains(PlayerName_tmp, regex=False, case=False)]
        else:
            return None

        self.ui.Team_ComboBox.clear()
        self.ui.Team_ComboBox.addItem("All Teams")
        self.ui.team_list = sorted(set(Stats_data_tmp["Team"]))
        for team in self.ui.team_list:
            if team != "Two Other Teams":
                self.ui.Team_ComboBox.addItem(team)

        self.ui.Season_ComboBox.clear()
        self.ui.Season_ComboBox.addItem("All Seasons")
        self.ui.season_list = sorted(set(Stats_data_tmp["Season"]))
        for season in self.ui.season_list:
            self.ui.Season_ComboBox.addItem(season)

    def Search_Button_Clicked(self, PlayerName, TeamName, SeasonName):
        # if PlayerName is None or PlayerName == "[All Players]":
        #     print("Please Choose Player!")
        #     return
        PlayerName_tmp, TeamName_tmp, SeasonName_tmp = PlayerName, TeamName, SeasonName
        if TeamName is None or SeasonName is None:
            return None
        if PlayerName == "All Players":
            PlayerName_tmp = ""
        if TeamName == "All Teams":
            TeamName_tmp = ""
        if SeasonName == "All Seasons":
            SeasonName_tmp = ""
        self.ui.Info_Table.clear()
        df_table = self.Stats_data_source.copy()
        df_table = df_table[df_table["Team"].str.contains(TeamName_tmp, regex=False)]
        df_table = df_table[df_table["Season"].str.contains(SeasonName_tmp, regex=False)]
        df_table = df_table[df_table["Player"].str.contains(PlayerName_tmp, regex=False)]
        # df_table = df_table[(df_table["Player"] == PlayerName)]

        if PlayerName != "All Players":
            if sum(df_table["BHOF"]) > 0:
                BHOF_RMK = "Yes"
            else:
                BHOF_RMK = "No"
            MVP_Season_List = sorted(df_table[df_table["Season_MVP"] == True]["Season"])
            if len(MVP_Season_List) > 0:
                MVP_Season_RMK = ", ".join(MVP_Season_List)
            else:
                MVP_Season_RMK = "None"
            self.ui.BHOF_Label.setText(BHOF_RMK)
            self.ui.MVP_Label.setText(MVP_Season_RMK)
        else:
            self.ui.BHOF_Label.setText("Not Applicable")
            self.ui.MVP_Label.setText("Not Applicable")

        df_table.drop(columns=['Season_MVP', 'BHOF', 'Tm'], inplace=True)
        df_table_nrows = df_table.shape[0]
        df_table_ncolumns = df_table.shape[1]
        df_table_columns_names = df_table.columns
        self.ui.Info_Table.setColumnCount(df_table_ncolumns)
        self.ui.Info_Table.setRowCount(df_table_nrows)
        self.ui.Info_Table.setHorizontalHeaderLabels(df_table_columns_names)
        for i in range(0, df_table_nrows):
            df_table_row_values_list = list(df_table.iloc[i])
            self.ui.Info_Table.setRowHeight(i, 1)
            for j in range(0, df_table_ncolumns):
                df_table_values_item = str(df_table_row_values_list[j])
                new_item = QTableWidgetItem(df_table_values_item)
                new_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.ui.Info_Table.setItem(i, j, new_item)
                self.ui.Info_Table.horizontalHeader().setSectionResizeMode(j, QHeaderView.ResizeToContents)
        print("Searching:", "[" + PlayerName + "]", "played with", "[" + TeamName + "]", "in", "[" + SeasonName + "]")
        if len(df_table) == 0:
            print("No Results!")
            print()

    def Reset_Button_Clicked(self):
        print("Resetting......")
        self.ui.Info_Table.clear()
        self.ui.Info_Table.setColumnCount(0)
        self.ui.Info_Table.setRowCount(0)

        self.ui.Player_ComboBox.clear()
        self.ui.Player_ComboBox.addItem("All Players")
        self.ui.player_list = sorted(set(self.Stats_data_source["Player"]))
        for player in self.ui.player_list:
            self.ui.Player_ComboBox.addItem(player)

        self.ui.Team_Filter_ComboBox.clear()
        self.ui.Team_Filter_ComboBox.addItem("All Teams")
        self.ui.Team_ComboBox.clear()
        self.ui.Team_ComboBox.addItem("All Teams")
        self.ui.team_list = sorted(set(self.Stats_data_source["Team"]))
        for team in self.ui.team_list:
            if team != "Two Other Teams":
                self.ui.Team_Filter_ComboBox.addItem(team)
                self.ui.Team_ComboBox.addItem(team)

        self.ui.Season_Filter_ComboBox.clear()
        self.ui.Season_Filter_ComboBox.addItem("All Seasons")
        self.ui.Season_ComboBox.clear()
        self.ui.Season_ComboBox.addItem("All Seasons")
        self.ui.season_list = sorted(set(self.Stats_data_source["Season"]))
        for season in self.ui.season_list:
            self.ui.Season_Filter_ComboBox.addItem(season)
            self.ui.Season_ComboBox.addItem(season)

        self.ui.KeyWord_Text.clear()
        self.ui.BHOF_Label.clear()
        self.ui.MVP_Label.clear()
        print("Done!")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    NBA_Player_Stats = AppWindow()
    NBA_Player_Stats.show()
    sys.exit(app.exec_())
    input("WillyF")
