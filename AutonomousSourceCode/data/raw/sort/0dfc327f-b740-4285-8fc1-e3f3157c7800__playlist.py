class Playlist():

    # this method will sort a playlist by filename alphabetically
    @staticmethod
    def sort_by_filename(playlist):
        return sorted(playlist)

    # this method will sort a playlist by title/alphabetically
    @staticmethod
    def sort_by_title(playlist):
        return sorted(playlist, key=lambda tup: tup[1])

    # this method will sort a playlist by genre/alphabetically
    @staticmethod
    def sort_by_genre(playlist):
        return sorted(playlist, key=lambda tup: tup[1])

    # this method will sort a playlist by artist/alphabetically
    @staticmethod
    def sort_by_artist(playlist):
        return sorted(playlist, key=lambda tup: tup[1])

    # this method will sort playlist by year
    @staticmethod
    def sort_by_year(playlist):
        try:
            return sorted(playlist, key=lambda tup: tup[1])
        except:
            return playlist
