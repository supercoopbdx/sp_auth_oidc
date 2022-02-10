# coding: utf-8
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    "name": "Authentication OpenID Connect",
    "version": "9.0.1.0.0",
    "license": "AGPL-3",
    "author": "ICTSTUDIO, André Schenkels",
    "website": "https://www.ictstudio.eu",
    "description": """OpenID Connect authentication""",
    "external_dependencies": {"python": ["jose", "cryptography"]},
    "depends": ["auth_oauth"],
    "data": [
        "views/auth_oauth_provider.xml",
    ],
}
