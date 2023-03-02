# SPDX-License-Identifier: Apache-2.0
"""Main for the xStudio control command."""

import sys
import argparse
import xstudio
from xstudio.connection import Connection
from xstudio.core import *

__version__ = xstudio.__version__

def control_main():
    """Do main function."""
    retval = 0
    parser = argparse.ArgumentParser(
        description=f"{__doc__} Controls xstudio.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-s", "--session", action="store",
        type=str,
        help="Host name.",
        default=None
    )

    parser.add_argument(
        "-H", "--host", action="store",
        type=str,
        help="Host name.",
        default=None
    )

    parser.add_argument(
        "-p", "--port", action="store",
        type=int,
        help="Port.",
        default=45500
    )

    parser.add_argument(
        "-r", "--require-sync", action="store_true",
        help="Downgrade FULL to SYNC.",
        default=False
    )

    parser.add_argument(
        "-i", "--info", action="store_true",
        help="Print connection info.",
        default=False
    )

    parser.add_argument(
        "-a", "--add-media", type=str, nargs="*", default=[],
        help="Add media."
    )

    parser.add_argument(
        "-d", "--debug", action="store_true",
        help="More debug info.",
        default=False
    )

    args = parser.parse_args()

    if args.session:
        m = RemoteSessionManager(remote_session_path())
        s = m.find(args.session)
        conn = Connection(debug=args.debug)
        conn.connect_remote(s.host(), s.port.port(), args.require_sync)

    elif args.host:
        conn = Connection(debug=args.debug)
        conn.connect_remote(args.host, args.port, args.require_sync)
    else:
        conn = Connection(debug=args.debug)
        conn.connect_remote("localhost", args.port, args.require_sync)

    if args.info:
        print(
            f"    App: {conn.app_type}\n    API: {conn.api_type}\nVersion: {conn.app_version}\nSession: {conn.api.app.session.name}\n"
        )
        print("Playlists:")
        for p in conn.api.app.session.playlists:
            print(f"\n  {p.name}")
            print("\n     Media:")
            for m in p.media:
                print(f"       {m.name} {m.media_source().name}")
                for s in m.media_sources:
                    print(f"         {s.name} {s.media_reference}")
            print("\n     Playheads:")
            for m in p.playheads:
                print(f"       {m.name}")
                print(f"         Playing: {m.playing}")
                print(f"         Looping: {m.looping}")
                print(f"        Position: {m.position}")
                print(f"         Forward: {m.play_forward}")
                print(f"            Mode: {m.play_mode}")

    for path in args.add_media:
        if not len(conn.api.app.session.playlists):
            conn.api.app.session.create_playlist()
        print(conn.api.app.session.playlists[0].add_media(path))



    conn.disconnect()

    sys.exit(retval)
