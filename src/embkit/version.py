import subprocess


def get_version():
    """Get version information including git details."""
    try:
        commit_hash = (
            subprocess.check_output(
                ["git", "rev-parse", "HEAD"], stderr=subprocess.DEVNULL
            )
            .decode()
            .strip()
        )
        commit = commit_hash[:8]
        branch = (
            subprocess.check_output(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"], stderr=subprocess.DEVNULL
            )
            .decode()
            .strip()
        )

        # Get remote URL
        remote_url = (
            subprocess.check_output(
                ["git", "config", "--get", "remote.origin.url"],
                stderr=subprocess.DEVNULL,
            )
            .decode()
            .strip()
        )

        # Convert SSH URLs to HTTPS format
        if remote_url.startswith("git@"):
            remote_url = remote_url.replace(":", "/").replace("git@", "https://")
        if remote_url.endswith(".git"):
            remote_url = remote_url[:-4]

        git_info = f"""├── commit: {commit}
├── branch: {branch}
└── remote: {remote_url}"""

        return f"embedding-kit version 0.1\n{git_info}"

    except (subprocess.CalledProcessError, FileNotFoundError):
        return "embedding-kit version 0.1"
