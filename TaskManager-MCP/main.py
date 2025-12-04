import os
import json
import asyncio
from mcp.server.fastmcp import FastMCP

from task_manager import (
    add_task,
    list_all_tasks,
    delete_task,
    complete_task
)

mcp = FastMCP("TaskManager-Tools")

@mcp.tool()
async def task_add(description: str, due_date: str = None) -> dict:
    """
    Add a new task with an optional due date.
    """
    return await asyncio.to_thread(add_task, description, due_date)


@mcp.tool()
async def task_list() -> dict:
    """
    List all stored tasks.
    """
    return await asyncio.to_thread(list_all_tasks)


@mcp.tool()
async def task_delete(task_id: int) -> dict:
    """
    Delete a task by ID.
    """
    return await asyncio.to_thread(delete_task, task_id)


@mcp.tool()
async def task_complete(task_id: int) -> dict:
    """
    Mark a task as completed.
    """
    return await asyncio.to_thread(complete_task, task_id)


if __name__ == "__main__":

    mcp.run(transport="stdio")
