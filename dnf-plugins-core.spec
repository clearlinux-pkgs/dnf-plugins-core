#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dnf-plugins-core
Version  : 2.1.5
Release  : 8
URL      : https://github.com/rpm-software-management/dnf-plugins-core/archive/2.1.5.tar.gz
Source0  : https://github.com/rpm-software-management/dnf-plugins-core/archive/2.1.5.tar.gz
Summary  : Core Plugins for DNF
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: dnf-plugins-core-python3
Requires: dnf-plugins-core-bin
Requires: dnf-plugins-core-locales
Requires: dnf-plugins-core-python
BuildRequires : cmake
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv
Patch1: 0001-Don-t-fail-if-the-locklist-is-not-defined.patch

%description
Core Plugins for DNF. This package enhances DNF with builddep, config-manager, copr, debug,
debuginfo-install, download, needs-restarting, repoclosure, repograph, repomanage and reposync
commands. Additionally provides generate_completion_cache passive plugin.

%package bin
Summary: bin components for the dnf-plugins-core package.
Group: Binaries

%description bin
bin components for the dnf-plugins-core package.


%package locales
Summary: locales components for the dnf-plugins-core package.
Group: Default

%description locales
locales components for the dnf-plugins-core package.


%package python
Summary: python components for the dnf-plugins-core package.
Group: Default
Requires: dnf-plugins-core-python3

%description python
python components for the dnf-plugins-core package.


%package python3
Summary: python3 components for the dnf-plugins-core package.
Group: Default
Requires: python3-core

%description python3
python3 components for the dnf-plugins-core package.


%prep
%setup -q -n dnf-plugins-core-2.1.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517533569
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DPYTHON_DESIRED=3
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1517533569
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
%find_lang dnf-plugins-core

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/dnf-utils-3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f dnf-plugins-core.lang
%defattr(-,root,root,-)

