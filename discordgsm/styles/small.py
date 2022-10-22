from discord import Embed
from discordgsm.styles.style import Style
from discordgsm.translator import t


class Small(Style):
    """Small style"""

    @property
    def display_name(self) -> str:
        return t('style.small.display_name', self.locale)

    @property
    def description(self) -> str:
        return t('style.small.description', self.locale)

    def embed(self) -> Embed:
        title, description, color = self.embed_data()
        embed = Embed(title=title, description=description, color=color)

        self.add_game_field(embed)
        self.add_address_field(embed)
        self.add_players_field(embed)

        embed.set_image(url=self.server.style_data.get('image_url'))
        embed.set_thumbnail(url=self.server.style_data.get('thumbnail_url'))

        self.set_footer(embed)

        return embed
