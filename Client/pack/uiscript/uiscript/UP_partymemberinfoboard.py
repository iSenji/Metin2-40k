import uiScriptLocale

ROOT = "d:/ymir work/ui/public/"

window = {
	"name" : "PartyMemeberInfoBoard",

	"x" : 0,
	"y" : 0,

	"width" : 156,
	"height" : 50,

	"children" :
	(

		{
			"name" : "StateButton",
			"type" : "button",

			"x" : 106+30,
			"y" : 0+6,

			"default_image" : "d:/ymir work/ui/game/windows/party_state_normal_01.sub",
			"over_image" : "d:/ymir work/ui/game/windows/party_state_normal_02.sub",
			"down_image" : "d:/ymir work/ui/game/windows/party_state_normal_03.sub",
		},

		{
			"name" : "NameSlot",
			"type" : "bar",
			"style" : ("not_pick",),

			"x" : 52,
			"y" : 0+7,
			"width" : 84,
			"height" : 17,
			"color" : 0x99000000,

			"children" :
			(
				{
					"name" : "LevelPrint",
					"type" : "text",

					"x" : 3,
					"y" : 2,

					"text" : "0",
				},
				{
					"name" : "NamePrint",
					"type" : "text",

					"x" : 3+27,
					"y" : 2,

					"text" : uiScriptLocale.PARTY_MEMBER_INFO_NAME,
				},
			),
		},
		{ "name" : "Face_Image", "type" : "image", "x" : 0+4, "y" : 0+4, "image" : "d:/ymir work/ui/game/windows/face_warrior.sub" },
		{ "name" : "Face_Slot", "type" : "image", "x" : 0, "y" : 0, "image" : "d:/ymir work/ui/game/windows/box_face.sub" },
		{
			"name" : "Gauge",
			"type" : "gauge",
			"style" : ("not_pick",),

			"x" : 52,
			"y" : 17+7,
			"width" : 84,
			"color" : "red",
		},
		{
			"name" : "GaugeEXP",
			"type" : "gauge",
			"style" : ("not_pick",),

			"x" : 52,
			"y" : 26+7,
			"width" : 84,
			"color" : "yellow",
		},
		{
			"name" : "ExperienceImage",
			"type" : "image",

			"x" : 0,
			"y" : 38,

			"image" : "d:/ymir work/ui/game/windows/party_affect_experience.sub",
		},
		{
			"name" : "AttackerImage",
			"type" : "image",

			"x" : 38,
			"y" : 38,

			"image" : "d:/ymir work/ui/game/windows/party_affect_attackgrade.sub",
		},
		{
			"name" : "DefenderImage",
			"type" : "image",

			"x" : 38,
			"y" : 38,

			"image" : "d:/ymir work/ui/game/windows/party_affect_defencegrade.sub",
		},
		{
			"name" : "BufferImage",
			"type" : "image",

			"x" : 38,
			"y" : 38,

			"image" : "d:/ymir work/ui/game/windows/party_affect_attackgrade.sub",
		},
		{
			"name" : "SkillMasterImage",
			"type" : "image",

			"x" : 38,
			"y" : 38,

			"image" : "d:/ymir work/ui/game/windows/party_affect_attackgrade.sub",
		},
		{
			"name" : "TimeBonusImage",
			"type" : "image",

			"x" : 38,
			"y" : 38,

			"image" : "d:/ymir work/ui/game/windows/party_affect_timebonus.sub",
		},
		{
			"name" : "RegenBonus",
			"type" : "image",

			"x" : 38,
			"y" : 38,

			"image" : "d:/ymir work/ui/game/windows/party_affect_regenbonus.sub",
		},
		{
			"name" : "IncreaseArea150",
			"type" : "image",

			"x" : 38,
			"y" : 38,

			"image" : "d:/ymir work/ui/game/windows/party_affect_increasearea_150.sub",
		},
		{
			"name" : "IncreaseArea200",
			"type" : "image",

			"x" : 38,
			"y" : 38,

			"image" : "d:/ymir work/ui/game/windows/party_affect_increasearea_200.sub",
		},

	),
}
