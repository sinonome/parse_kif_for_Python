class ShogiRecord:
    """
        kif ファイルをパースしたものの情報を格納するクラス。このクラスではパースはしない。
        * data (ShogiData) : 棋譜のメタ情報を格納する ex : 日付 対局場所
        * kif  (ShogiKif)  : 将棋の進行を格納する
    """
    def __init__(self, **param):
        """
            パースした情報をここで受け取りたい
            Parameters
            ----------
            ここに書いてください（テンプレ）
        """
        pass


class ShogiData:
    """
        kif ファイルのメタ情報の格納
        memo:
            getter を定義してあげて、指定が不正ならエラーかNoneを吐くって処理をしたい
    """
    pass


class ShogiKif:
    """
        対局の内容を格納する
    """