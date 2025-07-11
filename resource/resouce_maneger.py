import pygame

class ResouceManeger:
    """
    ゲーム内のリソース（画像など）を効率的に管理するクラス。
    シングルトンパターンで実装し、ゲーム全体で常に一つのインスタンスを共有する。
    """
    _instance = None
    
    # __new__ をオーバーライドして、常に同じインスタンスを返すようにする
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """
        初回インスタンス生成時に一度だけ呼ばれる初期化処理。
        画像キャッシュ用の辞書を初期化する。
        """
        # self.initialized は、複数回 __init__ が呼ばれるのを防ぐためのフラグ
        if not hasattr(self, 'initialized'):
            self.image_cache = {}
            self.initialized = True

    def load_image(self, path: str) -> pygame.Surface:
        """
        指定されたパスから画像を読み込む。
        
        一度読み込んだ画像はキャッシュに保存し、次回以降はキャッシュから返すことで
        メモリの節約と読み込み速度の向上を図る。

        Args:
            path (str): 画像ファイルへのパス

        Returns:
            pygame.Surface: 読み込んだ画像データ
        """
        if path in self.image_cache:
            # 既にキャッシュに画像があれば、それを返す
            return self.image_cache[path]
        else:
            # キャッシュになければ、画像を読み込んでキャッシュに保存してから返す
            try:
                image = pygame.image.load(path)
                # ディスプレイが初期化されていれば、パフォーマンスの良い形式に変換する
                if pygame.display.get_init():
                    image = image.convert_alpha()

                self.image_cache[path] = image
                return image
            except pygame.error as e:
                print(f"画像の読み込みに失敗しました: {path}")
                raise e


