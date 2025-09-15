from packaging import version

class FilterModule(object):
    def filters(self):
        return {
            'normalize_redmine_version': self.normalize_redmine_version,
            'detect_product': self.detect_product,
            'is_ruby_compatible': self.is_ruby_compatible,
        }

    def detect_product(self, redmine_version):
        """
        redmine_version から製品種別を判定
        - 先頭に 'v' がついていれば RedMica
        - それ以外は Redmine
        """
        if redmine_version.startswith("v"):
            return "redmica"
        return "redmine"

    def normalize_redmine_version(self, redmine_version):
        """
        Redmine: "6.0.5" -> "6.0"
        RedMica: "v3.2.4" -> "3.2"
        """
        v = redmine_version.lstrip('v')  # v がついていれば削除
        parts = v.split('.')
        return ".".join(parts[0:2])

    def is_ruby_compatible(self, redmine_version, ruby_version, mapping):
        """
        redmine_version: string (例: "6.0.5" or "v3.2.4")
        ruby_version: string (例: "2.7.1")
        mapping: dict (varsから読み込む compatible_ruby_versions)
        """
        product = self.detect_product(redmine_version)
        norm_ver = self.normalize_redmine_version(redmine_version)

        if product not in mapping:
            return False
        if norm_ver not in mapping[product]:
            return False

        for entry in mapping[product][norm_ver]:
            if ruby_version.startswith(entry['version']):
                if 'min' in entry:
                    if version.parse(ruby_version) >= version.parse(entry['min']):
                        return True
                else:
                    return True
        return False
