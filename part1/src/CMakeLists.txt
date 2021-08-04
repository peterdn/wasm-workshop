project (TestLibrary)

set(CMAKE_EXECUTABLE_SUFFIX ".html")

add_library (Library STATIC Library.cpp)

add_executable(App main.cpp)

target_link_libraries (App PUBLIC Library)
