# Welcome to xSTUDIO

xSTUDIO is a media playback and review application designed for professionals working in the film and TV post production industries, particularly the Visual Effects and Feature Animation sectors. xSTUDIO is focused on providing an intuitive, easy to use interface with a high performance playback engine at its core and C++ and Python APIs for pipeline integration and customisation for total flexibility.

## How it Works

xSTUDIO is built with a modern, flexible, and high-performance architecture.

*   **Core Engine (C++):** The core of xSTUDIO is written in C++17 for maximum performance. It uses the **C++ Actor Framework (CAF)** to manage concurrency, ensuring that the application remains responsive even when performing heavy I/O operations like loading large media files.
*   **Python API:** A comprehensive Python API allows for deep integration into existing pipelines. You can script and control xSTUDIO, and even extend its functionality using Python. The bindings are created using the powerful `pybind11` library.
*   **User Interface (Qt/QML):** The UI is built using the Qt framework with QML, which allows for a modern, fluid, and cross-platform user experience.
*   **Plugin Architecture:** xSTUDIO features a plugin-based architecture, making it easy to extend. You can add support for new media codecs, colour management systems, or even custom user interface components.

## Features

*   High-performance, multi-threaded playback engine.
*   Support for a wide range of image and video formats via FFmpeg and OpenImageIO.
*   Advanced colour management using OpenColorIO.
*   Extensive Python API for scripting and automation.
*   Modern, intuitive user interface built with Qt/QML.
*   Plugin-based architecture for easy extension.
*   Cross-platform support (Linux, with Windows and macOS on the roadmap).

## Building xSTUDIO

This release of xSTUDIO can be built on various Linux flavours. MacOS and Windows compatibility is not available yet but this work is on the roadmap for 2023.

We provide comprehensive build steps for 3 of the most popular Linux distributions.

* [CentOS 7](docs/build_guides/centos_7.md)
* [Rocky Linux 9.1](docs/build_guides/rocky_linux_9_1.md)
* [Ubuntu 22.04](docs/build_guides/ubuntu_22_04.md)

Note that the xSTUDIO user guide is built with Sphinx using the Read-The-Docs theme. The package dependencies for building the docs are somewhat onerous to install and as such we have ommitted these steps from the instructions and instead recommend that you turn off the docs build. Instead, we include the fully built docs (as html pages) as part of this repo and building xSTUDIO will install these pages so that they can be loaded into your browser via the Help menu in the main UI.

### Building with Docker

If you have Docker and the NVIDIA Container Toolkit installed, you can build and run xSTUDIO in a container.

1.  **Build the Docker image:**
    ```bash
    docker build -t dneg/xstudio .
    ```
2.  **Allow the container to access your X server:**
    ```bash
    sudo xhost +local:root
    ```
3.  **Run the container:**
    ```bash
    docker run --rm --it --gpus all -v /tmp/.X11-unix:/tmp/.X11-unix -ipc host dneg/xstudio bash
    ```

## Running xSTUDIO

Once you have built xSTUDIO, you can run it from the build directory:

```bash
./build/bin/xstudio.bin
```

If you are running inside a Docker container, you can start xSTUDIO with the same command from within the container's shell.

## Contributing

We welcome contributions to xSTUDIO! If you would like to contribute, please follow these steps:

1.  **Fork the repository** on GitHub.
2.  **Create a new branch** for your feature or bug fix.
3.  **Make your changes** and commit them with clear, descriptive messages.
4.  **Push your branch** to your fork.
5.  **Open a pull request** to the main xSTUDIO repository.

Please make sure to read the `CODE_REVIEW.md` file for an overview of the project's architecture and coding style.
