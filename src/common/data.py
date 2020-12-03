class ShogiPiece:
    """
        将棋の駒の記号を定義
    """
    king   = 1      # 玉
    rook   = 2      # 飛車
    bishop = 3      # 角
    gold   = 4      # 金
    silver = 5      # 銀
    knight = 6      # 桂馬
    lance  = 7      # 香車
    pawn   = 8      # 歩


class ShogiTurn:
    """
        手番の記号を定義
    """
    black = 0       # 先手
    white = 1       # 後手
