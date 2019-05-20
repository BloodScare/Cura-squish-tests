Feature: Profile Management

  Scenario: Creating Profile
    Given Cura has been started with preset configurations
    When I open Print Settings
    And I enable Gradual infill
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Profiles in preferences
    And I select Create profile
    And I give the new profile 'custom' name
    Then the profile overview contains the profile: 'custom #2'
	And I close the preferences

  Scenario: Duplicating Profile
    Given Cura is running
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Profiles in preferences
    Then the profile overview contains the profile: 'Fine'
    When I select the 'Fine' profile in preferences
    And I select Duplicate profile
    And I give the duplicated profile 'DuplicateOfFine' name
    Then the profile overview contains the profile: 'DuplicateOfFine'

#
#    Scenario: Exporting Profile
#       When I give the printer the '|any|' name
#
#    Scenario: Deleting Profile
#       When I give the printer the '|any|' name
#
#    Scenario: Importing Profile
#       When I give the printer the '|any|' name