import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd


class plot_players_img():
    def __init__(self, df, image_base):
        self.df = df
        self.image_base = image_base

    def plot(self):
        plt.subplots(figsize=(15, 10))
        for i in range(self.df.shape[0]):
            plt.subplot((int(self.df.shape[0]/3)+1), 3, i+1)
            img = mpimg.imread(self.image_base + str(self.df.loc[i, 'photo']) + '.png')
            imgplot = plt.imshow(img)
            plt.title(str(i+1)+ '.' + self.df.loc[i, 'full_name'] + '_' + self.df.loc[i, 'singular_name'] + '_' + str(self.df.loc[i, 'points_per_game']))
            plt.tick_params(left = False, right = False , labelleft = False ,labelbottom = False, bottom = False)
        return plt

class formation():
    def __init__(self, df, forward, midf, defend, goalk):
        self.df = df
        self.forward = forward
        self.midf = midf
        self.defend = defend
        self.goalk = goalk

    def players(self):
        df_f = self.df[(self.df.singular_name == 'Forward') & (self.df.status == 'a')].sort_values(by = 'points_by_diff', axis = 0, ascending  = False).head(self.forward).reset_index(drop =True)
        df_m = self.df[(self.df.singular_name == 'Midfielder') & (self.df.status == 'a')].sort_values(by = 'points_by_diff', axis = 0, ascending  = False).head(self.midf).reset_index(drop =True)
        df_d = self.df[(self.df.singular_name == 'Defender') & (self.df.status == 'a')].sort_values(by = 'points_by_diff', axis = 0, ascending  = False).head(self.defend).reset_index(drop =True)
        df_g = self.df[(self.df.singular_name == 'Goalkeeper') & (self.df.status == 'a')].sort_values(by = 'points_by_diff', axis = 0, ascending  = False).head(self.goalk).reset_index(drop =True)

        df_team = pd.concat([df_f, df_m, df_d, df_g], axis=0).reset_index(drop=True)

        return df_team
