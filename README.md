# Conditionals and Prediction Engines

Explain how an `if` statement decides, and how a language model decides, and
why the difference matters.

- [AI Use on This Assignment](#ai-use-on-this-assignment)
- [Setup](#setup)
- [Instructions](#instructions)
- [Short Response Questions](#short-response-questions)
  - [Prompt 1](#prompt-1)
- [Submitting](#submitting)

## AI Use on This Assignment

These are your own words. Do not use AI to draft or rewrite your responses —
that holds in every mode, including implementer mode. You may use it to check
grammar and spelling on writing you have already done, and you may use it
before you start to quiz you on how a model picks its next word.

There is something worth noticing here. This prompt asks you to explain how a
prediction engine works, and you have one available to ask. If you let it
write the explanation, you learn nothing about the thing you are writing
about. Paste this if you want it to quiz you instead:

> You are acting as a tutor. Quiz me on how a language model chooses its next
> token, and on how an if statement chooses a branch, until I can explain both
> without looking anything up. Tell me when my reasoning is wrong or
> imprecise. Do not write or rewrite any part of my response for me.

## Setup

Work in `development/mod-1`. Make a draft branch before you start.

```sh
git checkout -b draft
```

There is no code to run here. Pushing tells GitHub to check whether you have
written a response yet, which you can see in the **Actions** tab. That check
counts words. Your instructor reads what you wrote and replies on your pull
request.

## Instructions

Write your response in `short_response.md`. Aim for a response with these
qualities. Your instructor will give you feedback on each one:

- [ ] Addresses all parts of the prompt
- [ ] Accurately uses relevant technical terminology
- [ ] Is free of grammar and spelling mistakes (double check with Grammarly!)
- [ ] Uses markdown to enhance readability (preview in VS Code with
      Command/Control + Shift + V)
- [ ] Is easy to comprehend

## Short Response Questions

### Prompt 1

You have now written functions that decide things with `if` and `elif`, and
you have seen how a prediction engine decides what word comes next. Both are
making a choice. They make it in very different ways.

Write a short piece comparing the two. Cover all four of these:

- How a conditional statement decides which branch runs. Use the terms
  **control flow** and **conditional statement**.
- What it means that running `measure_rain(3)` a thousand times gives the same
  answer a thousand times.
- How a prediction engine arrives at its next word, and why running the same
  prompt twice can give you two different answers.
- One task you would trust an `if` statement with and would not trust a
  prediction engine with, and one where the opposite is true. Say why for
  each.

That last part is the one that matters most. Pick real examples and be
specific about what makes each tool right or wrong for the job.

There is no required length. Four honest paragraphs beat eight padded ones.

## Submitting

```sh
git add -A
git commit -m "your message"
git push
```

Open a pull request to your instructor for feedback.
