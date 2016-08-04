Name:       audio-config-sc
Summary:    audio configuration files
Version:    0.1.17
Release:    0
Group:      TO_BE/FILLED_IN
License:    Apache-2.0
BuildArch:  noarch
Source0:    audio-config-sc-%{version}.tar.gz
Requires(post): coreutils

%if "%{?tizen_target_name}" != "TM1"
ExcludeArch: noarch
%endif

%description
audio configuration files for spreadtrum devices such as ucm files.

%package kiran3G-sc7727
Summary: audio configuration files for kiran-3G-sc7727
Group: TO_BE/FILLED_IN
License:    Apache-2.0

%description kiran3G-sc7727
audio configuration files for kiran-3G-sc7727

%package TM1-sc7730
Summary: audio configuration files for TM1-sc7730
Group: TO_BE/FILLED_IN
License:    Apache-2.0

%description TM1-sc7730
audio configuration files for TM1-sc7730

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
mkdir -p %{buildroot}/usr/share/alsa/ucm/kiran3g-sc7727
mkdir -p %{buildroot}/usr/share/alsa/ucm/TM1-sc7730
mkdir -p %{buildroot}/usr/etc
mkdir -p %{buildroot}/opt/system
mkdir -p %{buildroot}/opt/etc/dump.d/module.d

cp -a LICENSE %{buildroot}/usr/share/license/kiran3g-sc7727
cp -a LICENSE %{buildroot}/usr/share/license/TM1-sc7730
cp -arf kiran-3G-sc7727/ucm/* %{buildroot}/usr/share/alsa/ucm/kiran3g-sc7727
cp -arf Z3-3G-sc7730/ucm/* %{buildroot}/usr/share/alsa/ucm/TM1-sc7730
cp -arf kiran-3G-sc7727/audio_para/audio_para %{buildroot}/usr/etc/audio_para.kiran
cp -arf Z3-3G-sc7730/audio_para/audio_para %{buildroot}/usr/etc/audio_para.tm1
cp -arf kiran-3G-sc7727/audio_para/audio_para %{buildroot}/opt/system/audio_para.kiran
cp -arf Z3-3G-sc7730/audio_para/audio_para %{buildroot}/opt/system/audio_para.tm1
cp -arf Z3-3G-sc7730/vbc_eq/vbc_eq %{buildroot}/opt/system/vbc_eq
cp -a util/regdump_sprd_audio.sh %{buildroot}/opt/etc/dump.d/module.d/

%pre kiran3G-sc7727
UCM_PATH=/usr/share/alsa/ucm
rm -rf $UCM_PATH/*
rm -rf /usr/etc/audio_para*
rm -rf /opt/system/audio_para*

%pre TM1-sc7730
UCM_PATH=/usr/share/alsa/ucm
rm -rf $UCM_PATH/*
rm -rf /usr/etc/audio_para*
rm -rf /opt/system/audio_para*
rm -rf /lib/firmware/vbc_eq

%post kiran3G-sc7727
UCM_PATH=/usr/share/alsa/ucm
ln -s $UCM_PATH/kiran3g-sc7727 $UCM_PATH/sprdphone
ln -s /usr/etc/audio_para.kiran /usr/etc/audio_para
ln -s /opt/system/audio_para.kiran /opt/system/audio_para

%post TM1-sc7730
UCM_PATH=/usr/share/alsa/ucm
ln -s $UCM_PATH/TM1-sc7730 $UCM_PATH/sprdphone
ln -s /usr/etc/audio_para.tm1 /usr/etc/audio_para
ln -s /opt/system/audio_para.tm1 /opt/system/audio_para
ln -s /opt/system/vbc_eq /lib/firmware/vbc_eq

%files kiran3G-sc7727
%manifest audio-config-sc.manifest
%defattr(-,root,root,-)
/usr/share/alsa/ucm/kiran3g-sc7727/*
/usr/etc/audio_para.kiran
/opt/system/audio_para.kiran
/opt/etc/dump.d/module.d/regdump_sprd_audio.sh
/usr/share/license/kiran3g-sc7727

%files TM1-sc7730
%manifest audio-config-sc.manifest
%defattr(-,root,root,-)
/usr/share/alsa/ucm/TM1-sc7730/*
/usr/etc/audio_para.tm1
/opt/system/audio_para.tm1
/opt/system/vbc_eq
/opt/etc/dump.d/module.d/regdump_sprd_audio.sh
/usr/share/license/TM1-sc7730
