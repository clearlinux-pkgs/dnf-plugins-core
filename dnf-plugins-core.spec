#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dnf-plugins-core
Version  : 4.0.14
Release  : 38
URL      : https://github.com/rpm-software-management/dnf-plugins-core/archive/4.0.14/dnf-plugins-core-4.0.14.tar.gz
Source0  : https://github.com/rpm-software-management/dnf-plugins-core/archive/4.0.14/dnf-plugins-core-4.0.14.tar.gz
Summary  : Core Plugins for DNF
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: dnf-plugins-core-libexec = %{version}-%{release}
Requires: dnf-plugins-core-license = %{version}-%{release}
Requires: dnf-plugins-core-locales = %{version}-%{release}
Requires: dnf-plugins-core-man = %{version}-%{release}
Requires: dnf-plugins-core-python = %{version}-%{release}
Requires: dnf-plugins-core-python3 = %{version}-%{release}
BuildRequires : Sphinx
BuildRequires : buildreq-cmake
BuildRequires : gettext-dev
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv
Patch1: 0001-Don-t-fail-if-the-locklist-is-not-defined.patch
Patch2: 0002-sphinx-build-3-does-not-exist.patch

%description
Core Plugins for DNF. This package enhances DNF with builddep, config-manager,
copr, debug, debuginfo-install, download, needs-restarting, repoclosure,
repograph, repomanage, reposync, changelog and repodiff commands. Additionally
provides generate_completion_cache passive plugin.

%package libexec
Summary: libexec components for the dnf-plugins-core package.
Group: Default
Requires: dnf-plugins-core-license = %{version}-%{release}

%description libexec
libexec components for the dnf-plugins-core package.


%package license
Summary: license components for the dnf-plugins-core package.
Group: Default

%description license
license components for the dnf-plugins-core package.


%package locales
Summary: locales components for the dnf-plugins-core package.
Group: Default

%description locales
locales components for the dnf-plugins-core package.


%package man
Summary: man components for the dnf-plugins-core package.
Group: Default

%description man
man components for the dnf-plugins-core package.


%package python
Summary: python components for the dnf-plugins-core package.
Group: Default
Requires: dnf-plugins-core-python3 = %{version}-%{release}

%description python
python components for the dnf-plugins-core package.


%package python3
Summary: python3 components for the dnf-plugins-core package.
Group: Default
Requires: python3-core

%description python3
python3 components for the dnf-plugins-core package.


%prep
%setup -q -n dnf-plugins-core-4.0.14
cd %{_builddir}/dnf-plugins-core-4.0.14
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585098633
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DPYTHON_DESIRED=3 -DWITH_MAN=0
make  %{?_smp_mflags}  ; make doc-man
popd

%install
export SOURCE_DATE_EPOCH=1585098633
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dnf-plugins-core
cp %{_builddir}/dnf-plugins-core-4.0.14/COPYING %{buildroot}/usr/share/package-licenses/dnf-plugins-core/4cc77b90af91e615a64ae04893fdffa7939db84c
pushd clr-build
%make_install
popd
%find_lang dnf-plugins-core
## Remove excluded files
rm -f %{buildroot}/usr/share/man/man1/*
rm -f %{buildroot}/usr/share/man/man5/yum-*
rm -f %{buildroot}/usr/share/man/man8/yum-*

%files
%defattr(-,root,root,-)

%files libexec
%defattr(-,root,root,-)
/usr/libexec/dnf-utils-3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dnf-plugins-core/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/dnf-builddep.8
/usr/share/man/man8/dnf-changelog.8
/usr/share/man/man8/dnf-config-manager.8
/usr/share/man/man8/dnf-copr.8
/usr/share/man/man8/dnf-debug.8
/usr/share/man/man8/dnf-debuginfo-install.8
/usr/share/man/man8/dnf-download.8
/usr/share/man/man8/dnf-generate_completion_cache.8
/usr/share/man/man8/dnf-leaves.8
/usr/share/man/man8/dnf-local.8
/usr/share/man/man8/dnf-needs-restarting.8
/usr/share/man/man8/dnf-post-transaction-actions.8
/usr/share/man/man8/dnf-repoclosure.8
/usr/share/man/man8/dnf-repodiff.8
/usr/share/man/man8/dnf-repograph.8
/usr/share/man/man8/dnf-repomanage.8
/usr/share/man/man8/dnf-reposync.8
/usr/share/man/man8/dnf-show-leaves.8
/usr/share/man/man8/dnf-versionlock.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f dnf-plugins-core.lang
%defattr(-,root,root,-)

