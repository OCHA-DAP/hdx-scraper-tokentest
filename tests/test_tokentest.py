from unittest.mock import patch


class TestTokenTest:
    def test_main(self, configuration):
        from hdx.scraper.tokentest.__main__ import main

        with patch(
            "hdx.scraper.tokentest.__main__.User.check_current_user_write_access"
        ) as mock_check:
            main()
            mock_check.assert_called_once_with("hdx")
