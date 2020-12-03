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


class Piece:
    """
        駒の情報を格納する
    """
    def __init__(
        self,
        piece: int,
        isGradeUp: bool = false,
        turn: int,
    ):
        """
            駒の情報の初期化
            Parameters
            ----------
            piece :
                駒の種類。int であれば何でもよいことにする
            nari  :
                成駒かどうか。true or false で
            turn  :
                だれの駒か。これも 0 or 1 だが詳細には限定しない。
        """
        self.piece = piece
        self.nari = isGradeUp
        self.turn = turn


# Other Vartex
NoPiece = Piece(None, False)