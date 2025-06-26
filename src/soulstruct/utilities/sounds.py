from __future__ import annotations

__all__ = ["sort_fmod_bank"]

import os
import re
import shutil
import subprocess
from pathlib import Path


def sort_fmod_bank(source_dir: Path | str, dest_dir: Path | str, make_voice_subfolders=True):
    """Sorts all files extracted from an FSB into `source_dir` into `dest_dir`, with a single WAV file extension.

    Files that start with "v###", where ### is any three-digit number, are placed into a subfolder called "v###" if
    `make_voice_subfolders=True` (default).
    """
    source_dir = Path(source_dir)
    dest_dir = Path(dest_dir)
    stem_re = re.compile(r"^(.*?)(.wav)+$")  # extension could be ".wav.wav" (e.g. from `fmod_extr.exe` output)
    voice_re = re.compile(r"^(v\d{3})\d*$")
    for source_path in Path(source_dir).glob("*.wav"):
        stem = stem_re.match(source_path.name).group(1)  # this regex can't fail, based on rglob string
        if (voice_match := voice_re.match(stem)) and make_voice_subfolders:
            this_dest_dir = dest_dir / voice_match.group(1)
        else:
            this_dest_dir = dest_dir
        this_dest_dir.mkdir(parents=True, exist_ok=True)
        dest_path = this_dest_dir / (stem + ".wav")
        shutil.move(source_path, dest_path)
        print(f"{source_path} -> {dest_path}")


def extract_fsb(fsb_path: Path | str, dest_dir: Path | str, make_voice_subfolders=True, fmod_extr_path=None):
    """Extract FSB and organize its contents into `dest_dir` using `sort_fmod_bank()`.

    The `fmod_extr.exe` utility (and its two required DLLs) must be next to the FSB file unless `fmod_extr_path` given.
    """
    fsb_path = Path(fsb_path)
    dest_dir = Path(dest_dir)
    if fmod_extr_path is None:
        fmod_extr_path = fsb_path.parent / "fmod_extr"
    else:
        fmod_extr_path = Path(fmod_extr_path)
    if list(dest_dir.glob("*.wav")):
        raise FileExistsError(
            "One or more '.wav' files already exist in dest directory. Cannot extract FSB until these are cleared up."
        )
    dest_dir.mkdir(parents=True, exist_ok=True)
    old_cwd = os.getcwd()
    try:
        os.chdir(str(dest_dir))
        retcode = subprocess.call([str(fmod_extr_path), str(fsb_path)])  # blocks until extraction completes
        if retcode == 0:
            sort_fmod_bank(dest_dir, dest_dir, make_voice_subfolders=make_voice_subfolders)
        else:
            raise RuntimeError("Error occurred in `fmod_extr.exe`.")
    finally:
        os.chdir(old_cwd)


FDP_VOICE_EVENT_TEMPLATE_DS1 = """<event>
    <name>{event_name}</name>
    <guid>{{09c075b4-ac48-48f6-a7f4-a5454053ac5e}}</guid>
    <parameter_nextid>0</parameter_nextid>
    <layer_nextid>0</layer_nextid>
    <layer>
        <name>parsed_layer0</name>
        <height>303</height>
        <envelope_nextid>0</envelope_nextid>
        <mute>0</mute>
        <solo>0</solo>
        <soundlock>0</soundlock>
        <envlock>0</envlock>
        <priority>-1</priority>
        <controlparameter>(distance)</controlparameter>
        <sound>
            <name>{sound_def_path}</name>
            <x>0</x>
            <width>1</width>
            <startmode>0</startmode>
            <loopmode>1</loopmode>
            <loopcount2>-1</loopcount2>
            <autopitchenabled>0</autopitchenabled>
            <autopitchparameter>0</autopitchparameter>
            <autopitchreference>0</autopitchreference>
            <autopitchatzero>0</autopitchatzero>
            <finetune>0</finetune>
            <volume>1</volume>
            <fadeintype>2</fadeintype>
            <fadeouttype>2</fadeouttype>
        </sound>
        <envelope>
            <name>parsed_envelope0</name>
            <dsp_name>Volume</dsp_name>
            <dsp_paramindex>0</dsp_paramindex>
            <colour>#7f0000</colour>
            <point>0,1,1,1</point>
            <point>1,0,0,1</point>
            <parametername>(distance)</parametername>
            <controlparameter>(distance)</controlparameter>
            <_PC_enable>1</_PC_enable>
            <_XBOX360_enable>1</_XBOX360_enable>
            <_XBOXONE_enable>1</_XBOXONE_enable>
            <_PSP_enable>1</_PSP_enable>
            <_PS3_enable>1</_PS3_enable>
            <_PS4_enable>1</_PS4_enable>
            <_WII_enable>1</_WII_enable>
            <_WiiU_enable>1</_WiiU_enable>
            <_3DS_enable>1</_3DS_enable>
            <_NGP_enable>1</_NGP_enable>
            <_ANDROID_enable>1</_ANDROID_enable>
            <_IOS_enable>1</_IOS_enable>
            <_BB10_enable>1</_BB10_enable>
            <mute>0</mute>
            <visible>1</visible>
            <hidden>0</hidden>
            <fromtemplate>No</fromtemplate>
            <mappingmethod>0</mappingmethod>
            <flags>0</flags>
            <exflags>0</exflags>
        </envelope>
        <envelope>
            <name>parsed_envelope1</name>
            <dsp_name>FMOD Lowpass Simple</dsp_name>
            <dsp_paramindex>0</dsp_paramindex>
            <colour>#7f0000</colour>
            <point>0,1,1,1</point>
            <point>1,0.766816,0,1</point>
            <parametername>(distance)</parametername>
            <controlparameter>(distance)</controlparameter>
            <_PC_enable>1</_PC_enable>
            <_XBOX360_enable>1</_XBOX360_enable>
            <_XBOXONE_enable>1</_XBOXONE_enable>
            <_PSP_enable>1</_PSP_enable>
            <_PS3_enable>1</_PS3_enable>
            <_PS4_enable>1</_PS4_enable>
            <_WII_enable>1</_WII_enable>
            <_WiiU_enable>1</_WiiU_enable>
            <_3DS_enable>1</_3DS_enable>
            <_NGP_enable>1</_NGP_enable>
            <_ANDROID_enable>1</_ANDROID_enable>
            <_IOS_enable>1</_IOS_enable>
            <_BB10_enable>1</_BB10_enable>
            <mute>0</mute>
            <visible>1</visible>
            <hidden>0</hidden>
            <fromtemplate>No</fromtemplate>
            <mappingmethod>1</mappingmethod>
            <flags>0</flags>
            <exflags>0</exflags>
        </envelope>
        <_PC_enable>1</_PC_enable>
        <_XBOX360_enable>1</_XBOX360_enable>
        <_XBOXONE_enable>1</_XBOXONE_enable>
        <_PSP_enable>1</_PSP_enable>
        <_PS3_enable>1</_PS3_enable>
        <_PS4_enable>1</_PS4_enable>
        <_WII_enable>1</_WII_enable>
        <_WiiU_enable>1</_WiiU_enable>
        <_3DS_enable>1</_3DS_enable>
        <_NGP_enable>1</_NGP_enable>
        <_ANDROID_enable>1</_ANDROID_enable>
        <_IOS_enable>1</_IOS_enable>
        <_BB10_enable>1</_BB10_enable>
    </layer>
    <parameter>
        <name>(distance)</name>
        <guid>{{c40bea9f-1317-4655-af6c-fad60e61a768}}</guid>
        <primary>1</primary>
        <loopmode>0</loopmode>
        <rangeunits></rangeunits>
        <rangemin>0</rangemin>
        <rangemax>27</rangemax>
        <rangespacing>2.7</rangespacing>
        <keyoffonsilence>0</keyoffonsilence>
        <velocity>0</velocity>
        <seekspeed>0</seekspeed>
    </parameter>
    <car_rpm>0</car_rpm>
    <car_rpmsmooth>0.075</car_rpmsmooth>
    <car_loadsmooth>0.05</car_loadsmooth>
    <car_loadscale>6</car_loadscale>
    <volume_db>0</volume_db>
    <pitch>0</pitch>
    <pitch_units>Semitones</pitch_units>
    <pitch_randomization>0</pitch_randomization>
    <pitch_randomization_units>Semitones</pitch_randomization_units>
    <volume_randomization>0</volume_randomization>
    <priority>128</priority>
    <maxplaybacks>1</maxplaybacks>
    <maxplaybacks_behavior>Steal_oldest</maxplaybacks_behavior>
    <stealpriority>10000</stealpriority>
    <mode>x_3d</mode>
    <ignoregeometry>No</ignoregeometry>
    <rolloff>Custom</rolloff>
    <mindistance>0</mindistance>
    <maxdistance>27</maxdistance>
    <auto_distance_filtering>Off</auto_distance_filtering>
    <distance_filter_centre_freq>1500</distance_filter_centre_freq>
    <headrelative>World_relative</headrelative>
    <oneshot>Yes</oneshot>
    <istemplate>No</istemplate>
    <usetemplate></usetemplate>
    <notes></notes>
    <userproperty>
        <name>playDistance</name>
        <guid>{{c44ec186-dbbd-40d5-9c96-4c3a39a6b219}}</guid>
        <description></description>
        <data_float>27</data_float>
        </userproperty>
    <userproperty>
        <name>stopDistance</name>
        <guid>{{5390d023-f3dc-4d15-85ce-3ce149af5aa6}}</guid>
        <description></description>
        <data_float>27</data_float>
    </userproperty>
    <userproperty>
        <name>returnType</name>
        <guid>{{f1e8acb7-0451-4d53-b0cb-7bdc10cd10a1}}</guid>
        <description></description>
        <data_int>1</data_int>
    </userproperty>
    <userproperty>
        <name>mixerNum</name>
        <guid>{{4f60c9bd-5529-4cd8-8bf7-572c961cf1ba}}</guid>
        <description></description>
        <data_int>1</data_int>
    </userproperty>
    <userproperty>
        <name>mixerID_0</name>
        <guid>{{49a8fc65-7b39-48ce-8fe3-45486f9c8690}}</guid>
        <description></description>
        <data_int>1</data_int>
    </userproperty>
    <category>Voice</category>
    <position_randomization_min>0</position_randomization_min>
    <position_randomization>0</position_randomization>
    <speaker_l>1</speaker_l>
    <speaker_c>0</speaker_c>
    <speaker_r>1</speaker_r>
    <speaker_ls>0</speaker_ls>
    <speaker_rs>0</speaker_rs>
    <speaker_lb>0</speaker_lb>
    <speaker_rb>0</speaker_rb>
    <speaker_lfe>0</speaker_lfe>
    <speaker_config>0</speaker_config>
    <speaker_pan_r>1</speaker_pan_r>
    <speaker_pan_theta>0</speaker_pan_theta>
    <cone_inside_angle>360</cone_inside_angle>
    <cone_outside_angle>360</cone_outside_angle>
    <cone_outside_volumedb>0</cone_outside_volumedb>
    <doppler_scale>1</doppler_scale>
    <reverbdrylevel_db>0</reverbdrylevel_db>
    <reverblevel_db>0</reverblevel_db>
    <speaker_spread>0</speaker_spread>
    <panlevel3d>1</panlevel3d>
    <fadein_time>0</fadein_time>
    <fadeout_time>0</fadeout_time>
    <spawn_intensity>1</spawn_intensity>
    <spawn_intensity_randomization>0</spawn_intensity_randomization>
    <TEMPLATE_PROP_LAYERS>1</TEMPLATE_PROP_LAYERS>
    <TEMPLATE_PROP_KEEP_EFFECTS_PARAMS>1</TEMPLATE_PROP_KEEP_EFFECTS_PARAMS>
    <TEMPLATE_PROP_VOLUME>0</TEMPLATE_PROP_VOLUME>
    <TEMPLATE_PROP_PITCH>1</TEMPLATE_PROP_PITCH>
    <TEMPLATE_PROP_PITCH_RANDOMIZATION>1</TEMPLATE_PROP_PITCH_RANDOMIZATION>
    <TEMPLATE_PROP_VOLUME_RANDOMIZATION>1</TEMPLATE_PROP_VOLUME_RANDOMIZATION>
    <TEMPLATE_PROP_PRIORITY>1</TEMPLATE_PROP_PRIORITY>
    <TEMPLATE_PROP_MAX_PLAYBACKS>1</TEMPLATE_PROP_MAX_PLAYBACKS>
    <TEMPLATE_PROP_MAX_PLAYBACKS_BEHAVIOR>1</TEMPLATE_PROP_MAX_PLAYBACKS_BEHAVIOR>
    <TEMPLATE_PROP_STEAL_PRIORITY>1</TEMPLATE_PROP_STEAL_PRIORITY>
    <TEMPLATE_PROP_MODE>1</TEMPLATE_PROP_MODE>
    <TEMPLATE_PROP_IGNORE_GEOMETRY>1</TEMPLATE_PROP_IGNORE_GEOMETRY>
    <TEMPLATE_PROP_X_3D_ROLLOFF>1</TEMPLATE_PROP_X_3D_ROLLOFF>
    <TEMPLATE_PROP_X_3D_MIN_DISTANCE>1</TEMPLATE_PROP_X_3D_MIN_DISTANCE>
    <TEMPLATE_PROP_X_3D_MAX_DISTANCE>1</TEMPLATE_PROP_X_3D_MAX_DISTANCE>
    <TEMPLATE_PROP_X_3D_POSITION>1</TEMPLATE_PROP_X_3D_POSITION>
    <TEMPLATE_PROP_X_3D_MIN_POSITION_RANDOMIZATION>1</TEMPLATE_PROP_X_3D_MIN_POSITION_RANDOMIZATION>
    <TEMPLATE_PROP_X_3D_POSITION_RANDOMIZATION>1</TEMPLATE_PROP_X_3D_POSITION_RANDOMIZATION>
    <TEMPLATE_PROP_X_3D_CONE_INSIDE_ANGLE>1</TEMPLATE_PROP_X_3D_CONE_INSIDE_ANGLE>
    <TEMPLATE_PROP_X_3D_CONE_OUTSIDE_ANGLE>1</TEMPLATE_PROP_X_3D_CONE_OUTSIDE_ANGLE>
    <TEMPLATE_PROP_X_3D_CONE_OUTSIDE_VOLUME>1</TEMPLATE_PROP_X_3D_CONE_OUTSIDE_VOLUME>
    <TEMPLATE_PROP_X_3D_DOPPLER_FACTOR>1</TEMPLATE_PROP_X_3D_DOPPLER_FACTOR>
    <TEMPLATE_PROP_REVERB_WET_LEVEL>1</TEMPLATE_PROP_REVERB_WET_LEVEL>
    <TEMPLATE_PROP_REVERB_DRY_LEVEL>1</TEMPLATE_PROP_REVERB_DRY_LEVEL>
    <TEMPLATE_PROP_X_3D_SPEAKER_SPREAD>1</TEMPLATE_PROP_X_3D_SPEAKER_SPREAD>
    <TEMPLATE_PROP_X_3D_PAN_LEVEL>1</TEMPLATE_PROP_X_3D_PAN_LEVEL>
    <TEMPLATE_PROP_X_2D_SPEAKER_L>1</TEMPLATE_PROP_X_2D_SPEAKER_L>
    <TEMPLATE_PROP_X_2D_SPEAKER_C>1</TEMPLATE_PROP_X_2D_SPEAKER_C>
    <TEMPLATE_PROP_X_2D_SPEAKER_R>1</TEMPLATE_PROP_X_2D_SPEAKER_R>
    <TEMPLATE_PROP_X_2D_SPEAKER_LS>1</TEMPLATE_PROP_X_2D_SPEAKER_LS>
    <TEMPLATE_PROP_X_2D_SPEAKER_RS>1</TEMPLATE_PROP_X_2D_SPEAKER_RS>
    <TEMPLATE_PROP_X_2D_SPEAKER_LR>1</TEMPLATE_PROP_X_2D_SPEAKER_LR>
    <TEMPLATE_PROP_X_2D_SPEAKER_RR>1</TEMPLATE_PROP_X_2D_SPEAKER_RR>
    <TEMPLATE_PROP_X_SPEAKER_LFE>1</TEMPLATE_PROP_X_SPEAKER_LFE>
    <TEMPLATE_PROP_ONESHOT>1</TEMPLATE_PROP_ONESHOT>
    <TEMPLATE_PROP_FADEIN_TIME>1</TEMPLATE_PROP_FADEIN_TIME>
    <TEMPLATE_PROP_FADEOUT_TIME>1</TEMPLATE_PROP_FADEOUT_TIME>
    <TEMPLATE_PROP_NOTES>1</TEMPLATE_PROP_NOTES>
    <TEMPLATE_PROP_USER_PROPERTIES>1</TEMPLATE_PROP_USER_PROPERTIES>
    <TEMPLATE_PROP_CATEGORY>0</TEMPLATE_PROP_CATEGORY>
    <_PC_enabled>1</_PC_enabled>
    <_XBOX360_enabled>1</_XBOX360_enabled>
    <_XBOXONE_enabled>1</_XBOXONE_enabled>
    <_PSP_enabled>1</_PSP_enabled>
    <_PS3_enabled>1</_PS3_enabled>
    <_PS4_enabled>1</_PS4_enabled>
    <_WII_enabled>1</_WII_enabled>
    <_WiiU_enabled>1</_WiiU_enabled>
    <_3DS_enabled>1</_3DS_enabled>
    <_NGP_enabled>1</_NGP_enabled>
    <_ANDROID_enabled>1</_ANDROID_enabled>
    <_IOS_enabled>1</_IOS_enabled>
    <_BB10_enabled>1</_BB10_enabled>
</event>
"""


def generate_fdp_voice_events(sound_def_paths, event_names=None):
    """Generate XML text to be pasted into an FDP file, where events are defined.

    By default, `event_names` defaults to the name at the end of each `sound_def_paths` entry.

    Use the "Regenerate GUIDs" option in the FMOD Designer right-click menu to create unique GUIDs for each new event
    (you can highlight them all at once). You probably won't get any adverse effects if you forget, though.
    """

    if event_names is not None and len(sound_def_paths) != len(event_names):
        raise ValueError("Length of `event_names` does not match length of `sound_def_paths`.")
    output = ""
    for i, sound_def_path in enumerate(sound_def_paths):
        if event_names is None:
            event_name = Path(sound_def_path).name
        else:
            event_name = event_names[i]
        output += FDP_VOICE_EVENT_TEMPLATE_DS1.format(event_name=event_name, sound_def_path=sound_def_path)
    print(output)


def main():
    sound_def_paths = [
        f"/frpg_sm18/v84400170{suffix}" for suffix in range(5)
    ]
    generate_fdp_voice_events(sound_def_paths)


if __name__ == '__main__':
    main()
