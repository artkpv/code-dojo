/// Codewars kata: Checking Groups
/// projectId=57a5a0d453ba33a293000939, solutionId=57a5a0d453ba33a29300093b

public static class Groups
{
    public static bool Check(string input)
    {
        return false;
    }
}

using NUnit.Framework;

[TestFixture]
public class GroupsTests
{
    [TestCase("()", true)]
    [TestCase("({", false)]
    public void Tests(string input, bool expected)
    {
        Assert.AreEqual(expected, Groups.Check(input));
    }
}


