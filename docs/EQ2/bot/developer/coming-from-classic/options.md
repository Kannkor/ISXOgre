# OgreBot option ids

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

Scripts and MCP buttons change OgreBot's options by id: `oc !c -ChangeOgreBotUIOption <who> <id> <value>`, `OgreBotAPI.Options:Set[<who>,<id>,<value>]`, or read one with `${OgreBotAPI.Options.Value[<id>]}`. Most ids are the same in the new bot (691 of them exist there). The ones below are Classic ids the new bot does not have.

> **:warning: Setting an id the new bot does not have does nothing**
>
> There is no error - the option just never changes. Do not swap in an id with a similar name: Classic has `checkbox_debug_casting`, `checkbox_debug_castingcompleted`, `checkbox_debug_castingdetails` and `checkbox_debug_castingextras` as four different options. If you need one of these, tell us.

## Never did anything - delete the line

These ids did nothing even in Classic (switched off there, or never an option at all). A line that sets one can go.

- `checkbox_other_handlefieldmedic`
- `checkbox_settings_doho`

## Not in the new bot (53)

- `checkbox_ascension_glacialfreeze_announce`
- `checkbox_ascension_glacialfreeze_announce_onlyifinraid`
- `checkbox_ascension_glacialfreeze_announce_toirc`
- `checkbox_ascension_glacialfreeze_noraidcomboing`
- `checkbox_autohunt_pullspell`
- `checkbox_debug_castingcompleted`
- `checkbox_debug_castingdetails`
- `checkbox_debug_castingextras`
- `checkbox_debug_chaintab`
- `checkbox_debug_fieldmedic`
- `checkbox_debug_internal_testing`
- `checkbox_defiler_maliciousspirits_primary`
- `checkbox_defiler_maliciousspirits_secondary`
- `checkbox_extra_moveraiddebuff`
- `checkbox_extra_raiddebuff`
- `checkbox_hud_raidoptions_test`
- `checkbox_load_ogreirc`
- `checkbox_load_ogreircinterface`
- `checkbox_load_ogreircuplink`
- `checkbox_loot_unpackdraconicphylactery`
- `checkbox_loot_unpackstatusbag`
- `checkbox_loot_unpackwarrunes`
- `checkbox_other_rezanyone`
- `checkbox_other_usecoldaincureall`
- `checkbox_overseer_threaded`
- `checkbox_pushover_auto_load`
- `checkbox_settings_autoattacktiming`
- `checkbox_settings_useblazingbowoflight`
- `checkbox_settings_waitforautoattack`
- `checkbox_setup_broadcasttellstouplink`
- `checkbox_setup_receivetellsfromuplink`
- `checkbox_timewarptiming_enabled`
- `checkbox_vampiricrequiem_allowincombat`
- `checkbox_vampiricrequiem_enable`
- `checkbox_vampiricrequiem_waittime`
- `combobox_autohunt_pullspell`
- `slider_timewarptiming_duration`
- `slider_timewarptiming_timeout`
- `textentry_aliases_alias_id`
- `textentry_ascensionembargo_delaytime`
- `textentry_ascensionembargo_embargotime`
- `textentry_hud_group_updateinterval`
- `textentry_hud_npc_updateinterval`
- `textentry_hud_pc_updateinterval`
- `textentry_hud_raid_updateinterval`
- `textentry_hud_raidoptions_updateinterval`
- `textentry_ogreconsole_height`
- `textentry_ogreconsole_width`
- `textentry_ogreconsole_x`
- `textentry_ogreconsole_y`
- `textentry_setup_turbo`
- `textentry_timewarp_timewarptext`
- `textentry_vampiricrequiem_waittime`
