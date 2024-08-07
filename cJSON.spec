#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v13
# autospec commit: dc0ff31
#
Name     : cJSON
Version  : 1.7.18
Release  : 5
URL      : https://github.com/DaveGamble/cJSON/archive/v1.7.18/cJSON-1.7.18.tar.gz
Source0  : https://github.com/DaveGamble/cJSON/archive/v1.7.18/cJSON-1.7.18.tar.gz
Summary  : Ultralightweight JSON parser in ANSI C
Group    : Development/Tools
License  : MIT
Requires: cJSON-lib = %{version}-%{release}
Requires: cJSON-license = %{version}-%{release}
BuildRequires : buildreq-cmake
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# cJSON
Ultralightweight JSON parser in ANSI C.
## Table of contents
* [License](#license)
* [Usage](#usage)
* [Welcome to cJSON](#welcome-to-cjson)
* [Building](#building)
* [Copying the source](#copying-the-source)
* [CMake](#cmake)
* [Makefile](#makefile)
* [Meson](#meson)
* [Vcpkg](#Vcpkg)
* [Including cJSON](#including-cjson)
* [Data Structure](#data-structure)
* [Working with the data structure](#working-with-the-data-structure)
* [Basic types](#basic-types)
* [Arrays](#arrays)
* [Objects](#objects)
* [Parsing JSON](#parsing-json)
* [Printing JSON](#printing-json)
* [Example](#example)
* [Printing](#printing)
* [Parsing](#parsing)
* [Caveats](#caveats)
* [Zero Character](#zero-character)
* [Character Encoding](#character-encoding)
* [C Standard](#c-standard)
* [Floating Point Numbers](#floating-point-numbers)
* [Deep Nesting Of Arrays And Objects](#deep-nesting-of-arrays-and-objects)
* [Thread Safety](#thread-safety)
* [Case Sensitivity](#case-sensitivity)
* [Duplicate Object Members](#duplicate-object-members)
* [Enjoy cJSON!](#enjoy-cjson)

%package dev
Summary: dev components for the cJSON package.
Group: Development
Requires: cJSON-lib = %{version}-%{release}
Provides: cJSON-devel = %{version}-%{release}
Requires: cJSON = %{version}-%{release}

%description dev
dev components for the cJSON package.


%package lib
Summary: lib components for the cJSON package.
Group: Libraries
Requires: cJSON-license = %{version}-%{release}

%description lib
lib components for the cJSON package.


%package license
Summary: license components for the cJSON package.
Group: Default

%description license
license components for the cJSON package.


%prep
%setup -q -n cJSON-1.7.18
cd %{_builddir}/cJSON-1.7.18
pushd ..
cp -a cJSON-1.7.18 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1719953513
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test
cd ../../buildavx2/clr-build-avx2;
make test || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1719953513
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cJSON
cp %{_builddir}/cJSON-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/cJSON/7953915bb3c653fd23ba9a96cbacabf2c005fad6 || :
cp %{_builddir}/cJSON-%{version}/tests/unity/docs/license.txt %{buildroot}/usr/share/package-licenses/cJSON/82d0bcdf2087a772a9517374e2df993d85fb447e || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/cjson/cJSON.h
/usr/lib64/cmake/cJSON/cJSONConfig.cmake
/usr/lib64/cmake/cJSON/cJSONConfigVersion.cmake
/usr/lib64/cmake/cJSON/cjson-relwithdebinfo.cmake
/usr/lib64/cmake/cJSON/cjson.cmake
/usr/lib64/libcjson.so
/usr/lib64/pkgconfig/libcjson.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libcjson.so.1.7.18
/usr/lib64/libcjson.so.1
/usr/lib64/libcjson.so.1.7.18

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cJSON/7953915bb3c653fd23ba9a96cbacabf2c005fad6
/usr/share/package-licenses/cJSON/82d0bcdf2087a772a9517374e2df993d85fb447e
