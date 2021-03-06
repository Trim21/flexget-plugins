from flexget_plugins.modify.magnet_add_dn import PluginMagnetAddDownloadName


def test_add_dn():
    assert PluginMagnetAddDownloadName.add_dn(
        "magnet:?xt=urn:btih:190F1ABAED7AE7252735A811149753AA83E34309",
        "URL Escaped Torrent Name",
    ) == (
        "magnet:?xt=urn:btih:190F1ABAED7AE7252735"
        "A811149753AA83E34309&dn=URL+Escaped+Torrent+Name"
    )
