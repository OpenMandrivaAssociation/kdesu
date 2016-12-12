%define major 5
%define libname %mklibname KF5KDESu %{major}
%define devname %mklibname KF5KDESu -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kdesu
Version: 5.29.0
Release: 1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: KDE Frameworks 5 library for obtaining superuser privileges
URL: http://kde.org/
License: GPL
Group: System/Libraries
# compile with fpie
Patch0: fpie.patch
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5Pty)
BuildRequires: cmake(KF5I18n)
Requires: %{libname} = %{EVRD}

%description
KDE Frameworks 5 library for obtaining superuser privileges.

%package -n %{libname}
Summary: KDE Frameworks 5 library for obtaining superuser privileges
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE Frameworks 5 library for obtaining superuser privileges.

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Desu library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Desu library.

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kdesud5

%files -f kdesud5.lang
%{_libdir}/libexec/kf5/kdesu_stub
%attr(2755,root,nogroup) %{_libdir}/libexec/kf5/kdesud

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_libdir}/qt5/mkspecs/modules/*.pri
