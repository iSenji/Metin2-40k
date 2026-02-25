#ifndef __MINING_H
#define __MINING_H

namespace mining
{
	LPEVENT CreateMiningEvent(LPCHARACTER ch, LPCHARACTER load, int count);
	DWORD GetRawOreFromLoad(DWORD dwLoadVnum);
	bool OreRefine(LPCHARACTER ch, LPCHARACTER npc, LPITEM item, int cost, int pct, LPITEM metinstone_item);
	int GetFractionCount();
#ifdef ENABLE_MINING_TIMER
	extern void MiningTimer(LPCHARACTER ch, BYTE miningType, BYTE miningTime)
#endif

	// REFINE_PICK
	int RealRefinePick(LPCHARACTER ch, LPITEM item);
	void CHEAT_MAX_PICK(LPCHARACTER ch, LPITEM item);
	// END_OF_REFINE_PICK

	bool IsVeinOfOre (DWORD vnum);
}

#endif
