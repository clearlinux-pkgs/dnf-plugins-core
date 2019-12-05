#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dnf-plugins-core
Version  : 4.0.6
Release  : 26
URL      : https://github.com/rpm-software-management/dnf-plugins-core/archive/4.0.6.tar.gz
Source0  : https://github.com/rpm-software-management/dnf-plugins-core/archive/4.0.6.tar.gz
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
%setup -q -n dnf-plugins-core-4.0.6
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552952251
mkdir -p clr-build
pushd clr-build
export LDFLAGS="${LDFLAGS} -fno-lto"
%cmake .. -DPYTHON_DESIRED=3 -DWITH_MAN=0
make  %{?_smp_mflags} ; make doc-man
popd

%install
export SOURCE_DATE_EPOCH=1552952251
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dnf-plugins-core
cp COPYING %{buildroot}/usr/share/package-licenses/dnf-plugins-core/COPYING
pushd clr-build
%make_install
popd
%find_lang dnf-plugins-core

%files
%defattr(-,root,root,-)

%files libexec
%defattr(-,root,root,-)
/usr/libexec/dnf-utils-3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dnf-plugins-core/COPYING

%files man
%defattr(0644,root,root,0755)
%exclude /usr/share/man/man1/debuginfo-install.1
%exclude /usr/share/man/man1/dnf-utils.1
%exclude /usr/share/man/man1/needs-restarting.1
%exclude /usr/share/man/man1/package-cleanup.1
%exclude /usr/share/man/man1/repo-graph.1
%exclude /usr/share/man/man1/repoclosure.1
%exclude /usr/share/man/man1/repodiff.1
%exclude /usr/share/man/man1/repomanage.1
%exclude /usr/share/man/man1/reposync.1
%exclude /usr/share/man/man1/yum-builddep.1
%exclude /usr/share/man/man1/yum-changelog.1
%exclude /usr/share/man/man1/yum-config-manager.1
%exclude /usr/share/man/man1/yum-debug-dump.1
%exclude /usr/share/man/man1/yum-debug-restore.1
%exclude /usr/share/man/man1/yumdownloader.1
%exclude /usr/share/man/man5/yum-changelog.conf.5
%exclude /usr/share/man/man5/yum-versionlock.conf.5
%exclude /usr/share/man/man8/yum-copr.8
%exclude /usr/share/man/man8/yum-versionlock.8
/usr/share/man/man8/dnf.plugin.builddep.8
/usr/share/man/man8/dnf.plugin.changelog.8
/usr/share/man/man8/dnf.plugin.config_manager.8
/usr/share/man/man8/dnf.plugin.copr.8
/usr/share/man/man8/dnf.plugin.debug.8
/usr/share/man/man8/dnf.plugin.debuginfo-install.8
/usr/share/man/man8/dnf.plugin.download.8
/usr/share/man/man8/dnf.plugin.generate_completion_cache.8
/usr/share/man/man8/dnf.plugin.leaves.8
/usr/share/man/man8/dnf.plugin.local.8
/usr/share/man/man8/dnf.plugin.migrate.8
/usr/share/man/man8/dnf.plugin.needs_restarting.8
/usr/share/man/man8/dnf.plugin.repoclosure.8
/usr/share/man/man8/dnf.plugin.repodiff.8
/usr/share/man/man8/dnf.plugin.repograph.8
/usr/share/man/man8/dnf.plugin.repomanage.8
/usr/share/man/man8/dnf.plugin.reposync.8
/usr/share/man/man8/dnf.plugin.show-leaves.8
/usr/share/man/man8/dnf.plugin.versionlock.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f dnf-plugins-core.lang
%defattr(-,root,root,-)

