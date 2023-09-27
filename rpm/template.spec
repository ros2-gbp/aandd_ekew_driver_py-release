%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-aandd-ekew-driver-py
Version:        0.0.2
Release:        3%{?dist}%{?release_suffix}
Summary:        ROS aandd_ekew_driver_py package

License:        Apache-2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-pyserial
Requires:       ros-humble-action-msgs
Requires:       ros-humble-rclpy
Requires:       ros-humble-weight-scale-interfaces
Requires:       ros-humble-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-humble-action-msgs
BuildRequires:  ros-humble-rclpy
BuildRequires:  ros-humble-ros-workspace
BuildRequires:  ros-humble-weight-scale-interfaces
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-humble-ament-copyright
BuildRequires:  ros-humble-ament-flake8
BuildRequires:  ros-humble-ament-pep257
%endif

%description
aandd ek/ew series driver python package

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/humble"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Wed Sep 27 2023 Jiaqing Lin <lin.jiaqing@techmagic.co.jp> - 0.0.2-3
- Autogenerated by Bloom

* Mon Sep 25 2023 Jiaqing Lin <lin.jiaqing@techmagic.co.jp> - 0.0.2-2
- Autogenerated by Bloom

* Tue Sep 19 2023 Jiaqing Lin <lin.jiaqing@techmagic.co.jp> - 0.0.2-1
- Autogenerated by Bloom

* Fri Sep 08 2023 Jiaqing Lin <lin.jiaqing@techmagic.co.jp> - 0.0.1-1
- Autogenerated by Bloom

