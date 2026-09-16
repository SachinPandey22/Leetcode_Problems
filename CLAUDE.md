# LeetCode Practice Workspace

## Purpose
This folder is used for daily LeetCode problem solving in Python.

## Working style
- Solve each problem in a single Python file named after the problem.
- Keep a `Solution` class with the required method signature.
- Include a runnable driver in the same file under `if __name__ == "__main__":`.
- Use sample tests and edge cases to verify behavior.
- Prefer clear, readable Python over clever or overly condensed code.
- Explain the approach briefly when asked, but keep the code implementation focused.
- Keep the repository workflow clean: do not mix LeetHub-synced work on `main` with personal practice work.

## Git workflow
- Remote: `https://github.com/SachinPandey22/Leetcode_Problems` (origin).
- `main` is the LeetHub-synced branch, auto-committed to directly by the LeetHub browser
  extension whenever a problem is solved on leetcode.com. Never check out or commit to
  `main` locally — LeetHub writes to it via the GitHub API, not local git, so a local
  checkout only risks stale/conflicting state.
- All local work (Striver A2Z / TUF problems, handwritten exercises, anything LeetCode
  doesn't have) happens on the `dsa-practice` branch, created from `origin/main`.
- `dsa-practice` intentionally does **not** track `origin/main` (upstream was unset after
  branch creation) so a plain `git push` can never land on `main` by accident. Push it
  explicitly: `git push -u origin dsa-practice` (first time), `git push` after that.
- Do not commit to `main` for local practice unless explicitly asked and the user
  understands the tradeoff.

## Expectations for Claude Code
- Generate a working Python solution for the given problem (LeetCode or Striver A2Z/TUF).
- Include a driver with representative test cases, including edge cases.
- Verify outputs by running the script when appropriate.
- Do not commit changes unless explicitly asked.
- Keep the solution scoped to the problem, without unrelated refactors.

## File conventions
- Use snake_case filenames such as `two_sum.py` or `merge_two_sorted_lists.py`.
- Use the standard LeetCode naming style for the class method when provided by the prompt.
- Keep the file self-contained and easy to run from the terminal.

## Review/verification
- Run the script after implementing the solution to confirm sample cases pass.
- If a problem requires multiple examples, include them in the driver as assertions or prints.
- If a solution is wrong or incomplete, revise it and re-run the checks.

## Non-goals
- No Git commits unless requested.
- No broad project scaffolding beyond this folder.
- No extra frameworks or dependency files unless the problem specifically requires them.
