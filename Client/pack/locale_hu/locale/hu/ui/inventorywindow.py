import uiScriptLocale
import item

EQUIPMENT_START_INDEX = 225
COSTUME_START_INDEX = item.COSTUME_SLOT_START
COSTUME_SLOT_WEAPON = item.COSTUME_SLOT_WEAPON


window = {
	"name" : "InventoryWindow",

	## 600 - (width + 오른쪽으로 부터 띄우기 24 px)
	"x" : SCREEN_WIDTH - 176,
	"y" : SCREEN_HEIGHT - 37 - 565,

	"style" : ("movable", "float", "alpha_sensitive"),

	"width" : 176+14,
	"height" : 565,

	"children" :
	(
		## Inventory, Equipment Slots
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0+14,
			"y" : 0,

			"width" : 176,
			"height" : 565,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 7,

					"width" : 161,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":77, "y":3, "text":uiScriptLocale.INVENTORY_TITLE, "text_horizontal_align":"center" },
					),
				},

				## Equipment Slot
				{
					"name" : "Equipment_Base",
					"type" : "image",

					"x" : 10,
					"y" : 33,

					# "image" : "d:/ymir work/ui/equipment_bg_with_ring.tga",
					"image" : "d:/ymir work/ui/equipment_bg_without_ring.tga",

					"children" :
					(

						{
							"name" : "EquipmentSlot",
							"type" : "slot",

							"x" : 3,
							"y" : 3,

							"width" : 150,
							"height" : 182,

							"slot" : (
										{"index":EQUIPMENT_START_INDEX+0, "x":39, "y":37, "width":32, "height":64},
										{"index":EQUIPMENT_START_INDEX+1, "x":39, "y":2, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+2, "x":39, "y":145, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+3, "x":75, "y":67, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+4, "x":3, "y":3, "width":32, "height":96},
										{"index":EQUIPMENT_START_INDEX+5, "x":114, "y":67, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+6, "x":114, "y":35, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+7, "x":2, "y":145, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+8, "x":75, "y":145, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+9, "x":114, "y":2, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+10, "x":75, "y":35, "width":32, "height":32},
										{"index":item.EQUIPMENT_BELT, "x":39, "y":106, "width":32, "height":32},
									),
						},
                        
						## Dragon Soul Button
						{
							"name" : "DSSButton",
							"type" : "button",

							"x" : 114,
							"y" : 107,

							"tooltip_text" : uiScriptLocale.TASKBAR_DRAGON_SOUL,

							"default_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_01.tga",
							"over_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_02.tga",
							"down_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_03.tga",
						},
						## MallButton
						{
							"name" : "MallButton",
							"type" : "button",

							"x" : 118,
							"y" : 148,

							"tooltip_text" : uiScriptLocale.MALL_TITLE,

							"default_image" : "d:/ymir work/ui/game/TaskBar/Mall_Button_01.tga",
							"over_image" : "d:/ymir work/ui/game/TaskBar/Mall_Button_02.tga",
							"down_image" : "d:/ymir work/ui/game/TaskBar/Mall_Button_03.tga",
						},
						## CostumeButton
						{
							"name" : "CostumeButton",
							"type" : "button",

							"x" : 78,
							"y" : 5,

							"tooltip_text" : uiScriptLocale.COSTUME_TITLE,

							"default_image" : "d:/ymir work/ui/game/costume_button_01.tga",
							"over_image" : "d:/ymir work/ui/game/costume_button_02.tga",
							"down_image" : "d:/ymir work/ui/game/costume_button_03.tga",
						},						
						{
							"name" : "Equipment_Tab_01",
							"type" : "radio_button",

							"x" : 86,
							"y" : 161,

							"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
							"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
							"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",

							"children" :
							(
								{
									"name" : "Equipment_Tab_01_Print",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"all_align" : "center",

									"text" : "I",
								},
							),
						},
						{
							"name" : "Equipment_Tab_02",
							"type" : "radio_button",

							"x" : 86 + 32,
							"y" : 161,

							"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
							"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
							"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",

							"children" :
							(
								{
									"name" : "Equipment_Tab_02_Print",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"all_align" : "center",

									"text" : "II",
								},
							),
						},

					),
				},
				{
					"name" : "Inventory_Tab_01",
					"type" : "radio_button",
		
					"x" : 10,
					"y" : 33 + 191,
		
					"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_1,
		
					"children" :
					(
						{
							"name" : "Inventory_Tab_01_Print",
							"type" : "text",
		
							"x" : 0,
							"y" : 0,
		
							"all_align" : "center",
		
							"text" : "I",
						},
					),
				},
				{
					"name" : "Inventory_Tab_02",
					"type" : "radio_button",
		
					"x" : 10 + 32,
					"y" : 33 + 191,
		
					"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_2,
		
					"children" :
					(
						{
							"name" : "Inventory_Tab_02_Print",
							"type" : "text",
		
							"x" : 0,
							"y" : 0,
		
							"all_align" : "center",
		
							"text" : "II",
						},
					),
				},
				{
					"name" : "Inventory_Tab_03",
					"type" : "radio_button",
		
					"x" : 10 + 32*2,
					"y" : 33 + 191,
		
					"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_2,
		
					"children" :
					(
						{
							"name" : "Inventory_Tab_03_Print",
							"type" : "text",
		
							"x" : 0,
							"y" : 0,
		
							"all_align" : "center",
		
							"text" : "III",
						},
					),
				},
				{
					"name" : "Inventory_Tab_04",
					"type" : "radio_button",
		
					"x" : 10 + 32*3,
					"y" : 33 + 191,
		
					"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_2,
		
					"children" :
					(
						{
							"name" : "Inventory_Tab_04_Print",
							"type" : "text",
		
							"x" : 0,
							"y" : 0,
		
							"all_align" : "center",
		
							"text" : "IV",
						},
					),
				},
				{
					"name" : "Inventory_Tab_05",
					"type" : "radio_button",
		
					"x" : 10 + 32*4,
					"y" : 33 + 191,
		
					"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_2,
		
					"children" :
					(
						{
							"name" : "Inventory_Tab_05_Print",
							"type" : "text",
		
							"x" : 0,
							"y" : 0,
		
							"all_align" : "center",
		
							"text" : "V",
						},
					),
				},
				## Costume Equipment Slot
				{
					"name" : "Costume_Base",
					"type" : "expanded_image",
					"x" : 10,
					"y" : 33,
					"image" : "d:/ymir work/ui/inventory_buttons/eq_cosmetics_page_v2.jpg",
					"children" :
					(
						{
							"name" : "CostumeSlot",
							"type" : "slot",
							"x" : 3,
							"y" : 3,
							"width" : 150,
							"height" : 182,
							"slot" : (
										{"index":COSTUME_START_INDEX+0, "x":61, "y":77, "width":32, "height":64},
										{"index":COSTUME_START_INDEX+1, "x":61, "y":40, "width":32, "height":32},
										{"index":COSTUME_START_INDEX+2, "x":10, "y":63, "width":32, "height":96},
										{"index":COSTUME_START_INDEX+4, "x":108, "y":23, "width":32, "height":32},#Sash
										{"index":COSTUME_START_INDEX+3, "x":108, "y":63, "width":32, "height":32},
									),
						},
					),
				},
				## Secondary Equipment Slot
				{
					"name" : "Secondary_Base",
					"type" : "expanded_image",
					"x" : 10,
					"y" : 33,
					"image" : "d:/ymir work/ui/inventory_buttons/eq_secondary_page_v2.jpg",
					"children" :
					(
						{
							"name" : "SecondarySlot",
							"type" : "slot",
							"x" : 3,
							"y" : 3,
							"width" : 150,
							"height" : 182,
							"slot" : (
									    {"index":item.EQUIPMENT_RING1, "x":8, "y":2, "width":32, "height":32},
										{"index":item.EQUIPMENT_RING2, "x":44, "y":2, "width":32, "height":32},
										{"index":item.EQUIPMENT_RING3, "x":8, "y":38, "width":32, "height":32},
										#{"index":COSTUME_START_INDEX+3, "x":115, "y":4, "width":32, "height":32},
									#	{"index":item.EQUIPMENT_PET, "x":115, "y":42, "width":32, "height":32},
									),
						},
					),
				},
				## Talisman Equipment Slot
				{
					"name" : "Talisman_Base",
					"type" : "expanded_image",
					"x" : 10,
					"y" : 33,
					"image" : "d:/ymir work/ui/inventory_buttons/eq_pendant_page.jpg",
					"children" :
					(
						{
							"name" : "TalismanSlot",
							"type" : "slot",
							"x" : 3,
							"y" : 3,
							"width" : 150,
							"height" : 182,
							"slot" : (
									#    {"index":COSTUME_START_INDEX+0, "x":61, "y":77, "width":32, "height":64},
									#    {"index":COSTUME_START_INDEX+1, "x":61, "y":40, "width":32, "height":32},
									#    {"index":COSTUME_START_INDEX+2, "x":61, "y":125, "width":32, "height":32},
									#    {"index":COSTUME_START_INDEX+3, "x":10, "y":62, "width":32, "height":96},
									#    {"index":COSTUME_START_INDEX+4, "x":110, "y":61, "width":32, "height":32},
									),
						},
					),
				},
				## Effect Equipment Slot
				{
					"name" : "Effect_Base",
					"type" : "expanded_image",
					"x" : 10,
					"y" : 33,
					"image" : "d:/ymir work/ui/inventory_buttons/eq_effect_page_v2.jpg",
					"children" :
					(
						{
							"name" : "EffectSlot",
							"type" : "slot",
							"x" : 3,
							"y" : 3,
							"width" : 150,
							"height" : 182,
							"slot" : (
									#    {"index":COSTUME_START_INDEX+0, "x":61, "y":77, "width":32, "height":64},
									#    {"index":COSTUME_START_INDEX+1, "x":61, "y":40, "width":32, "height":32},
									#    {"index":COSTUME_START_INDEX+2, "x":61, "y":125, "width":32, "height":32},
									#    {"index":COSTUME_START_INDEX+3, "x":10, "y":62, "width":32, "height":96},
									#    {"index":COSTUME_START_INDEX+4, "x":110, "y":61, "width":32, "height":32},
									),
						},
					),
				},
				## Item Slot
				{
					"name" : "ItemSlot",
					"type" : "grid_table",

					"x" : 8,
					"y" : 246,

					"start_index" : 0,
					"x_count" : 5,
					"y_count" : 9,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub"
				},

				## Print
				{
					"name":"Money_Slot",
					"type":"button",

					"x":8,
					"y":28,

					"horizontal_align":"center",
					"vertical_align":"bottom",

					"default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",

					"children" :
					(
						{
							"name":"Money_Icon",
							"type":"image",

							"x":-18,
							"y":2,

							"image":"d:/ymir work/ui/game/windows/money_icon.sub",
						},

						{
							"name" : "Money",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"horizontal_align" : "right",
							"text_horizontal_align" : "right",

							"text" : "123456789",
						},
					),
				},

			),
		},
		{
			"name" : "Costume_Tab_01",
			"type" : "radio_button",
			"x" : 0,
			"y" : 32,
			"default_image" : "d:/ymir work/ui/inventory_buttons/eqtabclosed.dds",
			"over_image" : "d:/ymir work/ui/inventory_buttons/eqtabclosed.dds",
			"down_image" : "d:/ymir work/ui/inventory_buttons/eqtabopen.dds",
			"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_1,
			"children" :
			(
				{
					"name" : "Equipment_Tab_01_Print",
					"type" : "text",
					"x" : 0,
					"y" : 0,
					"all_align" : "center",
					"text" : "I",
				},
			),
		},
		{
			"name" : "Costume_Tab_02",
			"type" : "radio_button",
			"x" : 0,
			"y" : 32 + 22,
			"default_image" : "d:/ymir work/ui/inventory_buttons/eqtabclosed.dds",
			"over_image" : "d:/ymir work/ui/inventory_buttons/eqtabclosed.dds",
			"down_image" : "d:/ymir work/ui/inventory_buttons/eqtabopen.dds",
			"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_2,
			"children" :
			(
				{
					"name" : "Equipment_Tab_02_Print",
					"type" : "text",
					"x" : 0,
					"y" : 0,
					"all_align" : "center",
					"text" : "II",
				},
			),
		},
		{
			"name" : "Costume_Tab_03",
			"type" : "radio_button",
			"x" : 0,
			"y" : 32 + 22*2,
			"default_image" : "d:/ymir work/ui/inventory_buttons/eqtabclosed.dds",
			"over_image" : "d:/ymir work/ui/inventory_buttons/eqtabclosed.dds",
			"down_image" : "d:/ymir work/ui/inventory_buttons/eqtabopen.dds",
			"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_3,
			"children" :
			(
				{
					"name" : "Equipment_Tab_03_Print",
					"type" : "text",
					"x" : 0,
					"y" : 0,
					"all_align" : "center",
					"text" : "III",
				},
			),
		},
		{
			"name" : "Costume_Tab_04",
			"type" : "radio_button",
			"x" : 0,
			"y" : 32 + 22*3,
			"default_image" : "d:/ymir work/ui/inventory_buttons/eqtabclosed.dds",
			"over_image" : "d:/ymir work/ui/inventory_buttons/eqtabclosed.dds",
			"down_image" : "d:/ymir work/ui/inventory_buttons/eqtabopen.dds",
			"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_4,
			"children" :
			(
				{
					"name" : "Equipment_Tab_04_Print",
					"type" : "text",
					"x" : 0,
					"y" : 0,
					"all_align" : "center",
					"text" : "IV",
				},
			),
		},
		{
			"name" : "Costume_Tab_05",
			"type" : "radio_button",
			"x" : 0,
			"y" : 32 + 22*4,
			"default_image" : "d:/ymir work/ui/inventory_buttons/eqtabclosed.dds",
			"over_image" : "d:/ymir work/ui/inventory_buttons/eqtabclosed.dds",
			"down_image" : "d:/ymir work/ui/inventory_buttons/eqtabopen.dds",
			"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_5,
			"children" :
			(
				{
					"name" : "Equipment_Tab_05_Print",
					"type" : "text",
					"x" : 0,
					"y" : 0,
					"all_align" : "center",
					"text" : "V",
				},
			),
		},
	),
}
