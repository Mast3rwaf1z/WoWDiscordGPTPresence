local MyAddon = {}

function MyAddon:OnEvent(event, ...)
  if event == "PLAYER_ENTERING_WORLD" or event == "ZONE_CHANGED_NEW_AREA" then
    
    -- Save variables
    MyAddonDB = MyAddonDB or {}
    MyAddonDB.zone = GetRealZoneText()
    MyAddonDB.name = UnitName("player")
    MyAddonDB.realm = GetRealmName():lower():gsub(" ", "-")
    MyAddonDB.class, _ = UnitClass("player")
    MyAddonDB.level = UnitLevel("player")
  end
end

local frame = CreateFrame("Frame")
frame:RegisterEvent("PLAYER_ENTERING_WORLD")
frame:RegisterEvent("ZONE_CHANGED_NEW_AREA")
frame:SetScript("OnEvent", MyAddon.OnEvent)
